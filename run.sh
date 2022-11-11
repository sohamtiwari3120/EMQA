python run_squad.py -rn trying_xlm_roberta_wandb \
      --model_type=xlm-roberta \
      --model_name=xlm-roberta-large  \
      --do_train \
      --do_eval \
      --do_lower_case \
      --train_file './data/tydiqa-goldp-v1.1-train.json' \
      --predict_file './data/tydiqa-goldp-v1.1-dev.json'  \
      --per_gpu_train_batch_size 4 \
      --per_gpu_eval_batch_size 4 \
      --learning_rate 3e-5  \
      --num_train_epochs 3  \
      --max_seq_length 384  \
      --doc_stride 128  \
      --output_dir './train_cache_output/' \
      --overwrite_cache --overwrite_output_dir
      

# python run_squad.py \
#       --model_type bert \
#       --model_name_or_path=bert-base-multilingual-uncased \
#       --do_train \
#       --do_eval \
#       --do_lower_case \
#       --train_file './data/tydiqa-goldp-v1.1-train.json' \
#       --predict_file './data/tydiqa-goldp-v1.1-dev.json' \
#       --per_gpu_train_batch_size 24 \
#       --per_gpu_eval_batch_size 24 \
#       --learning_rate 3e-5 \
#       --num_train_epochs 3 \
#       --max_seq_length 384 \
#       --doc_stride 128 \
#       --output_dir './train_cache_output/' \
#       --overwrite_cache
#       # --data_dir './data/' #\
