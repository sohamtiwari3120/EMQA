import os

def main():
    command_template= """
    python run_squad.py \
      --model_type bert \
      --model_name_or_path='./tbert_train_cache_output/' \
      --do_train \
      --do_eval \
      --do_lower_case \
      --train_file '{0}' \
      --predict_file './data/tydiqa-goldp-v1.1-dev.json' \
      --per_gpu_train_batch_size 24 \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './trilingual/{1}/' \
      --overwrite_output_dir \
      --run_name "{1}_trilingual_finetune_tsquad" \
      --overwrite_data_cache \
      --data_pkl_dir "home/sgowrira/EMQA2/EMQA/pkl5" 
      
      """
    file_path="./data"
    files=os.listdir(file_path)
    files=[l for l in files if '3_random_languages' in l]
    count=1
    for i in files:
        ft_path=os.path.join(file_path,i)
        os.system(command_template.format(ft_path,count))
        count=count+1
        
        
    

if __name__ == "__main__":
    main()