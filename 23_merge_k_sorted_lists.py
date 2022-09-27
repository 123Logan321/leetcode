class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for i in range(len(lists)):
            list_ind = lists[i]
            while list_ind is not None:
                values.append(list_ind.val)
                list_ind = list_ind.next
                
        values.sort(reverse=True)
        
        linked_list = None
        for value in values:
            linked_list = ListNode(int(value), linked_list)
        return linked_list