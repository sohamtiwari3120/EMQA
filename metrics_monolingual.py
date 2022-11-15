import os 

def main():
    
    command_template= """
    python run_squad.py \
      --model_type bert \
      --model_name_or_path='{0}' \
      --do_eval \
      --do_lower_case \
      --predict_file '{1}' \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './eval_cache_output/' \
      --overwrite_output_dir \
      --run_name "monolingual_{2}_finetune_tsquad_dev_lang_{3}" \
      --overwrite_data_cache \
      --data_pkl_dir "home/sgowrira/EMQA2/EMQA/pkl4" 
      
      """
    file_path="./monolingual"
    monolingual = os.listdir(file_path)
    for lang in monolingual:
        dev_data_path="./TyDiQA_dev_data"
        finetune_lang=lang.split("_")[-1]
        file=os.listdir(dev_data_path)
        base_model_path=os.path.join(file_path,lang)
        #print(os.path.join(file_path,lang))
        #print(finetune_lang)
        
        file = [l for l in file if '.json' in l]
        for eachfile in file:
            dev_lang=eachfile.split("-")[2]
            dev_file_path=os.path.join(dev_data_path,eachfile)
            os.system(command_template.format(base_model_path, dev_file_path, finetune_lang, dev_lang))
            #print(dev_lang)
        #print()
        


if __name__=="__main__":
    main()