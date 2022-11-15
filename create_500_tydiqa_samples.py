import os
import json
import random
import argparse

random.seed(123)


def main(args):
    file_path = "./TyDiQA_training_data"
    tydiqa_files = os.listdir(file_path)
    tydiqa_files = [l for l in tydiqa_files if '.json' in l]
    number_of_instances = args.number_of_instances
    out_path = f"./TyDiQA_{number_of_instances if number_of_instances !=-1 else 'full'}_training_data"
    os.makedirs(out_path, exist_ok=True)

    for tydiqa_file in tydiqa_files:
        language = (tydiqa_file.split("_")[1]).split(".")[0]
        # print(language)
        dataset = json.load(open(os.path.join(file_path, tydiqa_file)))
        data_len = len(dataset['data'])
        if number_of_instances != -1 and data_len >= number_of_instances:
            print(os.path.join(file_path, tydiqa_file), number_of_instances)
            dataset['data'] = random.sample(
                dataset['data'], number_of_instances)
        else:
            print(os.path.join(file_path, tydiqa_file), data_len)
            dataset['data'] = random.sample(
                dataset['data'], data_len)

        out_file_name = os.path.join(
            out_path, 'tydiqa_{}_{}.json'.format(language, number_of_instances))
        with open(out_file_name, 'w', encoding='utf-8') as outfile:
            json.dump(dataset, outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number_of_instances', type=int, default=500,
                        help="Number of instances to sample from each tydiqa lang train file. Enter -1 to sample all instances from each file.")
    args = parser.parse_args()
    main(args)
