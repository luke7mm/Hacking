//Copied while studying at http://javascript.algorithmexamples.com/web/Sorts/countingSort.html

//This work is not my own

function countingSort (arr, min, max) {
  let i
  let z = 0
  const count = []

  for (i = min; i <= max; i++) {
    count[i] = 0
  }

  for (i = 0; i < arr.length; i++) {
    count[arr[i]]++
  }

  for (i = min; i <= max; i++) {
    while (count[i]-- > 0) {
      arr[z++] = i
    }
  }

  return arr
}

const arr = [4, 5, 17, 29, 4, 22, 45, 19, 2, 55, 33, 66, 23, 5, 99]

console.log(arr)

console.log(countingSort(arr, 2, 99))