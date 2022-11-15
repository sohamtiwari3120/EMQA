import os

def main():
    path_template="./TyDiQA_4500_training_data/tydiqa_{0}_4500.json"
    languages=["arabic","bengali","english","finnish","indonesian","swahili","russian","telugu"]
    base_model_path='./tbert_train_cache_output/'
    command_template= """
    python run_squad.py \
      --model_type bert \
      --model_name_or_path='{0}' \
      --do_train \
      --do_eval \
      --do_lower_case \
      --train_file '{1}' \
      --predict_file './data/tydiqa-goldp-v1.1-dev.json' \
      --per_gpu_train_batch_size 24 \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir '{2}' \
      --overwrite_output_dir \
      --run_name "{3}_finetune_tsquad_base" \
      --overwrite_data_cache \
      --data_pkl_dir "home/sgowrira/EMQA2/EMQA/pkl4" 
      
      """
    
    for i in languages:
        ft_path=path_template.format(i)
        output_model_path = "./monolingual/fineTune_cache_output_{0}".format(i)
        os.system(command_template.format(base_model_path, ft_path, output_model_path, i))
        '''print('base model path ', base_model_path)
        print('train file ', ft_path)
        print('language ',i)
        print('output path ', output_model_path)
        print()'''
        #base_model_path=output_model_path
        
        
    

if __name__ == "__main__":
    main()