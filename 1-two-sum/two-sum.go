func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int)

    for i,num := range nums{
        bru := target - num
        if index, ok := numMap[bru]; ok {
            return []int{index,i}
        }
        numMap[num] = i
    }
    return []int{}
}
