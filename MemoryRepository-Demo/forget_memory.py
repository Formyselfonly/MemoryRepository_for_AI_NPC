import json, datetime
import random, copy
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.docstore.document import Document
from typing import List, Tuple, Optional
VECTOR_SEARCH_TOP_K = 6
LLM_HISTORY_LEN = 3
import math

def forgetting_curve(t, S):
    return math.exp(-t / 6*S)

    # # Example usage
    # t = 1  # Time elapsed since the information was learned (in days)
    # S = 7  # Strength of the memory

    # retention = forgetting_curve(t, S)
    # print("Retention after", t, "day(s):", retention)

class MemoryForgetterLoader(UnstructuredFileLoader):
    def __init__(self, filepath,language,mode="elements"):
        super().__init__(filepath, mode=mode)
        self.filepath = filepath
        self.memory_level = 3
        self.total_date = 30
        self.language = language
        self.memory_bank = {}
        
   
    def _get_date_difference(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"
        d1 = datetime.datetime.strptime(date1, date_format)
        d2 = datetime.datetime.strptime(date2, date_format)
        return (d2 - d1).days

     
    def update_memory_when_searched(self, recalled_memos,user,cur_date):
        for recalled in recalled_memos:
            recalled_id = recalled.metadata['memory_id']
            recalled_date = recalled_id.split('_')[1]
            for i,memory in enumerate(self.memory_bank[user]['history'][recalled_date]):
                if memory['memory_id'] == recalled_id:
                    self.memory_bank[user]['history'][recalled_date][i]['memory_strength'] += 1
                    self.memory_bank[user]['history'][recalled_date][i]['last_recall_date'] = cur_date
                    break
    
    def write_memories(self, out_file):
        with open(out_file, "w", encoding="utf-8") as f:
            print(f'Successfully write to {out_file}')
            json.dump(self.memory_bank, f, ensure_ascii=False, indent=4)
    
    def load_memories(self, memory_file):
        # print(memory_file)
        with open(memory_file, "r", encoding="utf-8") as f:
            self.memory_bank = json.load(f)

    def initial_load_forget_and_save(self,name,now_date):
        docs = []
        with open(self.filepath, "r", encoding="utf-8") as f:
            memories = json.load(f)
            for user_name, user_memory in memories.items():
                # if user_name != name:
                #     continue
                if 'history' not in user_memory.keys():
                    continue
                self.memory_bank[user_name] = copy.deepcopy(user_memory)
                for date, content in user_memory['history'].items():
                     memory_str = f'时间{date}的对话内容：' if self.language=='cn' else f'Conversation content on {date}:'
                     user_kw = '[|用户|]：' if self.language=='cn' else '[|User|]:'
                     ai_kw = '[|AI伴侣|]：' if self.language=='cn' else '[|AI|]:'
                     forget_ids = []
                     for i,dialog in enumerate(content):
                        tmp_str = memory_str
                        if not isinstance(dialog,dict):
                            dialog = {'query':dialog[0],'response':dialog[1]}
                            self.memory_bank[user_name]['history'][date][i] = dialog

                        query = dialog['query']
                        response = dialog['response']
                        memory_strength = dialog.get('memory_strength',1)
                        last_recall_date = dialog.get('last_recall_date',date)
                        memory_id = dialog.get('memory_id',f'{user_name}_{date}_{i}')
                        tmp_str += f'{user_kw} {query.strip()}; '
                        tmp_str += f'{ai_kw} {response.strip()}'
                        metadata = {'memory_strength':memory_strength,
                                    'memory_id':memory_id,'last_recall_date':last_recall_date,"source": memory_id}
                        
                        self.memory_bank[user_name]['history'][date][i].update(metadata)
                        days_diff = self._get_date_difference(last_recall_date, now_date)
                        retention_probability = forgetting_curve(days_diff,memory_strength)
                        print(days_diff,memory_strength,retention_probability)
                        # Keep the memory with the retention_probability
                        if random.random() > retention_probability:
                            forget_ids.append(i)
                            
                        else:
                            docs.append(Document(page_content=tmp_str,metadata=metadata))
                     print(user_name,date,forget_ids)
                     if len(forget_ids) > 0:
                         forget_ids.sort(reverse=True)
                         for idd in forget_ids:
                             self.memory_bank[user_name]['history'][date].pop(idd)
                     if len(self.memory_bank[user_name]['history'][date])==0:
                            self.memory_bank[user_name]['history'].pop(date)
                            self.memory_bank[user_name]['summary'].pop(date)
                     if 'summary' in self.memory_bank[user_name].keys():
                        if date in self.memory_bank[user_name]['summary'].keys():
                            if not isinstance(self.memory_bank[user_name]["summary"][date],dict):
                                self.memory_bank[user_name]["summary"][date] = {'content':self.memory_bank[user_name]["summary"][date]}
                            summary_str = self.memory_bank[user_name]["summary"][date]["content"] if isinstance(self.memory_bank[user_name]["summary"][date],dict) else self.memory_bank[user_name]["summary"][date]
                            summary = f'时间{date}的对话总结为：{summary_str}' if self.language=='cn' else f'The summary of the conversation on {date} is: {summary_str}'
                            memory_strength = self.memory_bank[user_name]['summary'][date].get('memory_strength',1) 
                            last_recall_date = self.memory_bank[user_name]["summary"][date].get('last_recall_date',date) 
                            metadata = {'memory_strength':memory_strength,
                                    'memory_id':f'{user_name}_{date}_summary','last_recall_date':last_recall_date,"source":f'{user_name}_{date}_summary'}
                            if isinstance(self.memory_bank[user_name]["summary"][date],dict):    
                                self.memory_bank[user_name]['summary'][date].update(metadata)
                            else:
                                self.memory_bank[user_name]['summary'][date] = {'content':self.memory_bank[user_name]['summary'][date],**metadata}
                            docs.append(Document(page_content=summary,metadata=metadata))
        self.write_memories(self.filepath) 
        return docs

    
def get_docs_with_score(docs_with_score):
    docs=[]
    for doc, score in docs_with_score:
        doc.metadata["score"] = score
        docs.append(doc)
    return docs


def seperate_list(ls: List[int]) -> List[List[int]]:
    lists = []
    ls1 = [ls[0]]
    for i in range(1, len(ls)):
        if ls[i-1] + 1 == ls[i]:
            ls1.append(ls[i])
        else:
            lists.append(ls1)
            ls1 = [ls[i]]
    lists.append(ls1)
    return lists

