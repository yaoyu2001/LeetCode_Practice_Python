# -*- coding:utf-8 -*-
"""
Description:大变双向字典树
迭代次数默认最大999，可以增加但是没必要。其实能深到999层，那这个序列还是选择另外的处理方式吧。

@author: WangLeAi
@date: 2018/8/15
"""


class TrieNode(object):
    def __init__(self, value=None, count=0, parent=None):
        # 值
        self.value = value
        # 频数统计
        self.count = count
        # 父结点
        self.parent = parent
        # 子节点，{value:TrieNode}
        self.children = {}


class Trie(object):
    def __init__(self):
        # 创建空的根节点
        self.root = TrieNode()

    def insert(self, sequence):
        """
        基操，插入一个序列
        :param sequence: 列表
        :return:
        """
        cur_node = self.root
        for item in sequence:
            if item not in cur_node.children:
                # 插入结点
                child = TrieNode(value=item, count=1, parent=cur_node)
                cur_node.children[item] = child
                cur_node = child
            else:
                # 更新结点
                cur_node = cur_node.children[item]
                cur_node.count += 1

    def search(self, sequence):
        """
        基操，查询是否存在完整序列
        :param sequence: 列表
        :return:
        """
        cur_node = self.root
        mark = True
        for item in sequence:
            if item not in cur_node.children:
                mark = False
                break
            else:
                cur_node = cur_node.children[item]
        # 如果还有子结点，说明序列并非完整
        if cur_node.children:
            mark = False
        return mark

    def delete(self, sequence):
        """
        基操，删除序列，准确来说是减少计数
        :param sequence: 列表
        :return:
        """
        mark = False
        if self.search(sequence):
            mark = True
            cur_node = self.root
            for item in sequence:
                cur_node.children[item].count -= 1
                if cur_node.children[item].count == 0:
                    cur_node.children.pop(item)
                    break
                else:
                    cur_node = cur_node.children[item]
        return mark

    def search_part(self, sequence, prefix, suffix, start_node=None):
        """
        递归查找子序列，返回前缀和后缀结点
        此处简化操作，仅返回一位前后缀的内容与频数
        :param sequence: 列表
        :param prefix: 前缀字典，初始传入空字典
        :param suffix: 后缀字典，初始传入空字典
        :param start_node: 起始结点，用于子树的查询
        :return:
        """
        if start_node:
            cur_node = start_node
            prefix_node = start_node.parent
        else:
            cur_node = self.root
            prefix_node = self.root
        mark = True
        # 必须从第一个结点开始对比
        for i in range(len(sequence)):
            if i == 0:
                if sequence[i] != cur_node.value:
                    for child_node in cur_node.children.values():
                        self.search_part(sequence, prefix, suffix, child_node)
                    mark = False
                    break
            else:
                if sequence[i] not in cur_node.children:
                    for child_node in cur_node.children.values():
                        self.search_part(sequence, prefix, suffix, child_node)
                    mark = False
                    break
                else:
                    cur_node = cur_node.children[sequence[i]]
        if mark:
            if prefix_node.value:
                # 前缀数量取序列词中最后一词的频数
                if prefix_node.value in prefix:
                    prefix[prefix_node.value] += cur_node.count
                else:
                    prefix[prefix_node.value] = cur_node.count
            for suffix_node in cur_node.children.values():
                if suffix_node.value in suffix:
                    suffix[suffix_node.value] += suffix_node.count
                else:
                    suffix[suffix_node.value] = suffix_node.count
            # 即使找到一部分还需继续查找子结点
            for child_node in cur_node.children.values():
                self.search_part(sequence, prefix, suffix, child_node)


if __name__ == "__main__":
    trie = Trie()
    texts = [["葬爱", "少年", "葬爱", "少年", "慕周力", "哈哈"], ["葬爱", "少年", "阿西吧"], ["烈", "烈", "风", "中"], ["忘记", "了", "爱"],
             ["埋葬", "了", "爱"]]
    for text in texts:
        trie.insert(text)
    markx = trie.search(["忘记", "了", "爱"])
    print(markx)
    markx = trie.search(["忘记", "了"])
    print(markx)
    markx = trie.search(["忘记", "爱"])
    print(markx)
    markx = trie.delete(["葬爱", "少年", "王周力"])
    print(markx)
    prefixx = {}
    suffixx = {}
    trie.search_part(["葬爱", "少年"], prefixx, suffixx)
    print(prefixx)
    print(suffixx)
