class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String string : strs) {
            if (string.length() > 99) {
                res.append(string.length());
            } else if ( string.length() == 0) {
                res.append("000");
            } else if (string.length() > 9) {
                res.append("0" + string.length());
            } else {
                res.append("00" + string.length());

            }
            res.append(string);
        }
        return res.toString();
    }
    public List<String> decode(String str) {
        ArrayList<String> stringList = new ArrayList<String>();
        int firstIndex = 0;
        int secondIndex = 3;
            System.out.println(str);
        while (secondIndex < str.length() + 1) {
            // read substring length
            int length = Integer.parseInt(str.substring(firstIndex, secondIndex));
            // read substring
            if (length == 0) {
                stringList.add("");
            }
            else {
                stringList.add(str.substring(firstIndex + 3, secondIndex + length));
            }
            // reset index
            firstIndex += length + 3;
            secondIndex += length + 3;
        }
        return stringList;
    }
}
