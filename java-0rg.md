Here is the extracted information from the image, formatted cleanly in Markdown while preserving the original layout structure.
1. First Non-Repeated Character
Find the first character in a string that does not repeat.
String str = "swiss";
Character result = str.chars()
    .mapToObj(c -> (char) c)
    .filter(c -> str.indexOf(c) != str.lastIndexOf(c))
    .findFirst()
    .orElse(null);
System.out.println(result);

 * Output: w
 * Time: O(n) | Space: O(1)
2. First Repeated Character
Find the first character in a string that repeats.
String str = "swiss";
Character result = str.chars()
    .mapToObj(c -> (char) c)
    .filter(c -> str.indexOf(c) != str.lastIndexOf(c))
    .findFirst()
    .orElse(null);
System.out.println(result);

 * Output: s
 * Time: O(n) | Space: O(1)
3. Remove Duplicates from List
Remove duplicate elements from a list.
List<Integer> numbers = Arrays.asList(10, 20, 10, 30, 20, 40);
List<Integer> result = numbers.stream()
    .distinct()
    .collect(Collectors.toList());
System.out.println(result);

 * Output: [10, 20, 30, 40]
 * Time: O(n) | Space: O(n)
4. Frequency of Characters
Find the frequency of each character in a string.
String str = "programming";
Map<Character, Long> freq = str.chars()
    .mapToObj(c -> (char) c)
    .collect(Collectors.groupingBy(
        Function.identity(),
        LinkedHashMap::new,
        Collectors.counting()));
System.out.println(freq);

 * Output: {p=1, r=2, o=1, g=2, a=1, m=2, i=1, n=1}
 * Time: O(n) | Space: O(n)
5. Second-Highest Number
Find the second highest number in a list of integers.
List<Integer> numbers = Arrays.asList(10, 50, 20, 80, 80, 30);
Integer secondHighest = numbers.stream()
    .distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1)
    .findFirst()
    .orElse(null);
System.out.println(secondHighest);

 * Output: 50
 * Time: O(n \log n) | Space: O(n)
6. Find Duplicate Elements
Find all duplicate elements in a list.
List<Integer> numbers = Arrays.asList(10, 20, 30, 20, 40, 10);
Set<Integer> seen = new HashSet<>();
Set<Integer> duplicates = numbers.stream()
    .filter(n -> !seen.add(n))
    .collect(Collectors.toSet());
System.out.println(duplicates);

 * Output: [10, 20]
 * Time: O(n) | Space: O(n)
7. Two Sum
Find two numbers whose sum equals the target.
int[] nums = {2, 7, 11, 15};
int target = 9;
Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (map.containsKey(complement)) {
        System.out.println(map.get(complement) + ", " + i);
        break;
    }
    map.put(nums[i], i);
}

 * Output: 0, 1
 * Time: O(n) | Space: O(n)
8. Longest Substring Without Repeating Characters
Find length of the longest substring without repeating characters.
String str = "abcabcbb";
Set<Character> set = new HashSet<>();
int left = 0, maxLength = 0;
for (int right = 0; right < str.length(); right++) {
    while (set.contains(str.charAt(right))) {
        set.remove(str.charAt(left));
        left++;
    }
    set.add(str.charAt(right));
    maxLength = Math.max(maxLength, right - left + 1);
}
System.out.println(maxLength);

 * Output: 3
 * Time: O(n) | Space: O(\min(n, m)) (m = character set size)
🌟 STREAM API - IMPORTANT PROBLEMS
| # | Problem | Stream Code Snippet | Output |
|---|---|---|---|
| 1 | Find Even Numbers | List<Integer> result = numbers.stream().filter(n -> n % 2 == 0).collect(Collectors.toList()); | [2, 4, 6, 8] |
| 2 | Find Maximum | int max = numbers.stream().max(Integer::compareTo).orElse(0); | 88 |
| 3 | Find Minimum | int min = numbers.stream().min(Integer::compareTo).orElse(0); | 2 |
| 4 | Sort Ascending | List<Integer> result = numbers.stream().sorted().collect(Collectors.toList()); | [1, 2, 3, 4, 5] |
| 5 | Sort Descending | List<Integer> result = numbers.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList()); | [5, 4, 3, 2, 1] |
| 6 | Sum of Numbers | int sum = numbers.stream().mapToInt(Integer::intValue).sum(); | 150 |
| 7 | Count > 50 | long count = numbers.stream().filter(n -> n > 50).count(); | 3 |
| 8 | Convert to Uppercase | List<String> result = names.stream().map(String::toUpperCase).collect(Collectors.toList()); | [RAM, SAM, JOHN] |
| 9 | Find Duplicate Strings | Set<String> seen = new HashSet<>(); 
 Set<String> duplicates = names.stream().filter(n -> !seen.add(n)).collect(Collectors.toSet()); | [RAM, SAM] |
| 10 | Group by Department | Map<String, List<Employee>> result = employees.stream().collect(Collectors.groupingBy(Employee::getDepartment)); | {HR=[...], IT=[...], FIN=[...]} |
| 11 | Highest Salary | Employee e = employees.stream().max(Comparator.comparing(Employee::getSalary)).orElse(null); | Employee[salary=90000] |
| 12 | Second-Highest Salary | Employee e = employees.stream().sorted(Comparator.comparing(Employee::getSalary).reversed()).skip(1).findFirst().orElse(null); | Employee[salary=70000] |
💡 INTERVIEW TIPS
 * Understand the problem clearly.
 * Start with brute force, then optimize.
 * Handle edge cases (null, empty, single element, all duplicates).
 * Explain your approach before coding.
 * Analyze Time & Space Complexity.
 * Use meaningful variable names.
 * Test with different inputs.
⏱️ COMMON TIME & SPACE COMPLEXITY
| Operation | Time Complexity | Space Complexity |
|---|---|---|
| Traversal / Search | O(n) | O(1) |
| Sorting | O(n \log n) | O(1) / O(n) |
| Hash Operations | O(1) avg | O(n) |
| Nested Loops | O(n^2) | O(1) |
| Recursion (n levels) | O(n) | O(n) |
| Sliding Window | O(n) | O(\min(n, m)) |
| Stream Operations | Depends (usually O(n)) | O(n) |
🎯 KEY TAKEAWAYS
 * Master String, Arrays, Collections.
 * Sliding Window is key for substring problems.
 * Hashmap / Set solve many real problems.
 * Streams improve code readability & conciseness.
 * Always think about optimization.
 * Practice + Patterns = Confidence!
USEFUL STREAM METHODS
filter()    map()    distinct()    sorted()    collect()    groupingBy()    counting()    reduce()
Would you like to explore or test the implementation of any specific algorithm or Stream API operation from this sheet?
