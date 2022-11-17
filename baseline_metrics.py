import os 

def main():
    languages = ["arabic", "bengali", "english", "finnish",
                 "indonesian", "korean", "russian", "swahili", "telugu"]
    eval_cmd_template = """python run_squad.py \
      --model_type bert \
      --model_name_or_path='{mnp}' \
      --do_eval \
      --do_lower_case \
      --predict_file './TyDiQA_dev_data/tydiqa-goldp-{lang}-v1.1-dev.json' \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './eval_cache_output/' \
      --overwrite_output_dir \
      --run_name 'final_baseline_f1_score_{lang}' \
      --overwrite_data_cache \
      --data_pkl_dir "home/sgowrira/EMQA2/EMQA/pkl6"
    """
    model_name_or_path = "./train_cache_output/"
    for lang in languages:
        print(f"Starting eval on language: {lang}")
        cmd = eval_cmd_template.format(lang=lang, mnp = model_name_or_path)
        print(f"Return code: {os.system(cmd)}\n\n")
        


if __name__=="__main__":
    main()