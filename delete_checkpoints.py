import os

def main():
    dir = "/home/ubuntu/EMQA/train_cache_output_eng+tsquad_att_test/checkpoint-{}/"
    save_steps = 500
    for i in range(23000, 28500, 500):
        del_dir = dir.format(i)
        # os.remove(del_dir)
        print(f"rm -rf {del_dir}")
        if os.system(f"rm -rf {del_dir}") != 0:
            break

if __name__ == "__main__":
    main()