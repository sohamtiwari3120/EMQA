# python run_squad.py -rn trying_xlm_roberta_wandb \
#       --model_type=xlm-roberta \
#       --model_name=xlm-roberta-large  \
#       --do_train \
#       --do_eval \
#       --do_lower_case \
#       --train_file './data/tydiqa-goldp-v1.1-train.json' \
#       --predict_file './data/tydiqa-goldp-v1.1-dev.json'  \
#       --per_gpu_train_batch_size 4 \
#       --per_gpu_eval_batch_size 4 \
#       --learning_rate 3e-5  \
#       --num_train_epochs 3  \
#       --max_seq_length 384  \
#       --doc_stride 128  \
#       --output_dir './train_cache_output/' \
#       --overwrite_cache --overwrite_output_dir
      

# python run_squad.py -rn trying_bert_tsquad\
#       --model_type bert \
#       --model_name_or_path=bert-base-multilingual-uncased \
#       --do_train \
#       --do_eval \
#       --do_lower_case \
#       --train_file './data/merged_squad_google_transltate/squad_plus_translatedSquad_.json' \
#       --predict_file './data/tydiqa-goldp-v1.1-dev.json' \
#       --per_gpu_train_batch_size 24 \
#       --per_gpu_eval_batch_size 24 \
#       --learning_rate 3e-5 \
#       --num_train_epochs 3 \
#       --max_seq_length 384 \
#       --doc_stride 128 \
#       --output_dir './train_cache_output/' \
#       --overwrite_cache
      # --data_dir './data/' #\
# --hf_name "sohamtiwari3120/train_cache_output_eng+tsquad_att_test"
python run_squad.py       --model_type bert    --hf_name "sohamtiwari3120/engsquad_tsquad_pretrain"   --model_name_or_path='/home/ubuntu/EMQA/train_cache_output_eng+tsquad_att_test/checkpoint-16500'    --do_train          --do_eval       --do_lower_case       --train_file '/home/ubuntu/EMQA/data/merged_squad_google_transltate/squad_plus_translatedSquad_.json'       --predict_file './data/tydiqa-goldp-v1.1-dev.json'       --per_gpu_train_batch_size 24       --per_gpu_eval_batch_size 24       --learning_rate 3e-5       --num_train_epochs 3       --max_seq_length 384       --doc_stride 128       --output_dir './train_cache_output_eng+tsquad_att_test/' --run_name "attempttest_train_eng+tsquad" --overwrite_output_dir --split_data_into_batches_and_save -doc -1 -pthi -pthe

# python run_squad.py       --model_type bert       --model_name_or_path='/home/ubuntu/EMQA/train_cache_output_eng+tsquad_att1/checkpoint-35000'       --do_train       --do_eval       --do_lower_case       --train_file '/home/ubuntu/EMQA/data/merged_squad_google_transltate/squad_plus_translatedSquad_.json'       --predict_file './data/tydiqa-goldp-v1.1-dev.json'       --per_gpu_train_batch_size 4       --per_gpu_eval_batch_size 4       --learning_rate 3e-5       --num_train_epochs 3       --max_seq_length 384       --doc_stride 128       --output_dir './train_cache_output_eng+tsquad_att1/' --run_name "attempt2_train_eng+tsquad" --overwrite_output_dir --split_data_into_batches_and_save -doc 11500
