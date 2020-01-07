/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 *Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 *You may assume that each input would have exactly one solution, and you may not use the same element twice.
 *Example:
 *Given nums = [2, 7, 11, 15], target = 9,
 *Because nums[0] + nums[1] = 2 + 7 = 9,
 *return [0, 1].
 */

//using enumerate create list with index and value [0 2] 和 hash table (dict) using oppiste way to store index and value {2:0.7:1}

/*
  [2,7,11,15] target 9
  r1:h{}
    0 2
    9-2=7 not in h
    h[2]=0
    h{2:0}
  r2:h{2:0}
     1 7
     9-7=2 in h
     return [h[2]=0,1]
*/
var twoSum = function(nums, target) {
    var h = {};
    for (const[index,value] of nums.entries()){
        if ((target-value) in h){
            return [h[target-value],index]
        }
        h[value]=index;
    };
    console.log(h)
};
