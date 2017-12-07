import jieba
import sys

def TextProcessor(text):
    seg_list = jieba.cut_for_search(text)
    print(" / ".join(seg_list))

def main(argv):
    TextProcessor('採用可提升隔音性的橢圓形耳罩，長時間使用依然能舒適監聽。')

if __name__ == '__main__':
    main(sys.argv)