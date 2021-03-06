# encoding: utf-8
import os
import socket
import sys
if sys.version_info.major == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 当前工作目录
hostname = socket.gethostname()
if hostname.lower().startswith("l-mbookpro") or hostname.startswith("192.168."):
    CWD = "/Users/l/Projects/Python/KDD/KDD_Workspace"
elif hostname.lower() == "precision":
    CWD = "/home/zhenghang/Projects/KDD"
else:
    assert(0)
# CWD = "/home/username/KDD/KDD_benchmark" # Linux系统目录
# CWD = "D:\KDD\KDD_Benchmark" # Windows系统目录

__period = "train"
# __period = "handle"

DATA_PATH = os.path.join(CWD, "data")
DATASET_PATH = os.path.join(DATA_PATH, "dataset")

# 训练和测试文件（训练阶段有验证数据，测试阶段使用测试数据）
if __period == "train":
    TRAIN_FILE = os.path.join(DATASET_PATH, "train_set", "Train.csv")
    TEST_FILE = os.path.join(DATASET_PATH, "valid_set", "Valid.csv")
    GOLD_FILE = os.path.join(DATASET_PATH, "valid_set", "Valid.gold.csv")
else:
    TRAIN_FILE = os.path.join(DATASET_PATH, "train_set", "Train.csv")
    TEST_FILE = os.path.join(DATASET_PATH, "test_set", "Test.02.csv")
    GOLD_FILE = ""

# 模型文件
MODEL_PATH = os.path.join(CWD, "model", "kdd.model")
# 训练和测试特征文件
TRAIN_FEATURE_PATH = os.path.join(CWD, "feature", "train.feature")
TEST_FEATURE_PATH = os.path.join(CWD, "feature", "test.feature")
# 分类在测试集上的预测结果
TEST_RESULT_PATH = os.path.join(CWD, "predict", "test.result")
# 重新格式化的预测结果
TEST_PREDICT_PATH = os.path.join(CWD, "predict", "test.predict")

COAUTHOR_FILE = os.path.join(DATASET_PATH, "coauthor.json")
PAPERIDAUTHORID_TO_NAME_AND_AFFILIATION_FILE = os.path.join(DATASET_PATH, "paperIdAuthorId_to_name_and_affiliation.json")
PAPERAUTHOR_FILE = os.path.join(DATASET_PATH, "PaperAuthor.csv")
AUTHOR_FILE = os.path.join(DATASET_PATH, "Author.csv")
PAPER_FILE = os.path.join(DATASET_PATH, "Paper.csv")
AUTHOR_ON_JOURNAL_FILE = os.path.join(DATASET_PATH, "authOnJournal.json")
AUTHOR_ON_CONFERENCE_FILE = os.path.join(DATASET_PATH, "authOnConference.json")

EXPORT_DIR = os.path.join(CWD, "export")
EXPORT_TEST_CSV_PATH = os.path.join(EXPORT_DIR, "Test.P02.csv")