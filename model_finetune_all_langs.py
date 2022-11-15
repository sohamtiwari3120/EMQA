import os
cmd_template = """python run_squad.py \
      --model_type bert \
      --model_name_or_path='/home/ubuntu/EMQA/train_cache_output_eng+tsquad_att_test/checkpoint-43500' \
      --do_train \
      --do_finetune \
      --do_eval \
      --do_lower_case \
      --train_file '/home/ubuntu/EMQA/TyDiQA_4500_training_data/tydiqa_{lang}_4500.json' \
      --predict_file '/home/ubuntu/EMQA/TyDiQA_dev_data/tydiqa-goldp-{lang}-v1.1-dev.json' \
      --per_gpu_train_batch_size 24 \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './4500_{lang}_fineTune_cache_output/' \
      --overwrite_output_dir \
      --run_name 'eng_tsquad_mono_ft_{lang}_4500_eval_{lang}' -sd -sdc -dpr  '/home/ubuntu/EMQA/TyDiQA_4500_training_data/tydiqa_{lang}_4500_pkls'
"""


def main():
    languages = ["arabic", "bengali", "english", "finnish",
                 "indonesian", "korean", "russian", "swahili", "telugu"]
    for lang in languages:
        print(f"Starting language: {lang}")
        cmd = cmd_template.format(lang=lang)
        print(f"Return code: {os.system(cmd)}\n\n")


def uniform_budget_finetune():
    finetune_cmd_template = """python run_squad.py \
      --model_type bert \
      --model_name_or_path='{mnp}' \
      --do_train \
      --do_finetune \
      --do_lower_case \
      --train_file '/home/ubuntu/EMQA/TyDiQA_500_training_data/tydiqa_{lang}_500.json' \
      --predict_file '/home/ubuntu/EMQA/TyDiQA_dev_data/tydiqa-goldp-{lang}-v1.1-dev.json' \
      --per_gpu_train_batch_size 24 \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './uniform_500_all_langs_finetune_cache_output/' \
      --overwrite_output_dir \
      --run_name 'eng_tsquad_uniform_ft_{lang}_500' -sd -sdc -dpr  '/home/ubuntu/EMQA/TyDiQA_500_training_data/tydiqa_{lang}_500_pkls'
    """
    languages = ["arabic", "bengali", "english", "finnish",
                 "indonesian", "korean", "russian", "swahili", "telugu"]
    model_name_or_path = "/home/ubuntu/EMQA/train_cache_output_eng+tsquad_att_test/checkpoint-43500"
    for lang in languages:
        print(f"Starting finetuning on language: {lang}")
        cmd = finetune_cmd_template.format(lang=lang, mnp = model_name_or_path)
        print(f"Return code: {os.system(cmd)}\n\n")
        model_name_or_path = "./uniform_500_all_langs_finetune_cache_output/"

    # getting eval metrics
    eval_cmd_template = """python run_squad.py \
      --model_type bert \
      --model_name_or_path='{mnp}' \
      --do_eval \
      --do_finetune \
      --do_lower_case \
      --train_file '/home/ubuntu/EMQA/TyDiQA_500_training_data/tydiqa_{lang}_500.json' \
      --predict_file '/home/ubuntu/EMQA/TyDiQA_dev_data/tydiqa-goldp-{lang}-v1.1-dev.json' \
      --per_gpu_train_batch_size 24 \
      --per_gpu_eval_batch_size 24 \
      --learning_rate 3e-5 \
      --num_train_epochs 3 \
      --max_seq_length 384 \
      --doc_stride 128 \
      --output_dir './uniform_500_all_langs_finetune_cache_output/' \
      --overwrite_output_dir \
      --run_name 'eng_tsquad_uniform_ft_{lang}_500_eval_{lang}' -sd -sdc -dpr  '/home/ubuntu/EMQA/TyDiQA_500_training_data/tydiqa_{lang}_500_pkls'
    """
    for lang in languages:
        print(f"Starting eval on language: {lang}")
        cmd = eval_cmd_template.format(lang=lang, mnp = model_name_or_path)
        print(f"Return code: {os.system(cmd)}\n\n")
        model_name_or_path = "./uniform_500_all_langs_finetune_cache_output/"


if __name__ == "__main__":
    uniform_budget_finetune()
