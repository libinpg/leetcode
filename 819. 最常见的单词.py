class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph+='.'
        pointer1 = pointer2 = 0
        map = {}
        flag =  0
        while pointer2 < len(paragraph):
            #如果当前指针是字母，则指针移动一位，指针最后落在非字母的第一位
            while  paragraph[pointer2].isalpha():
                pointer2+=1
            temp=paragraph[pointer1:pointer2].lower()
            if temp in map.keys():
                map[temp] += 1
            else:
                map[temp] = 1
            #如果当前指针不是字母,则指针移动一位，指针最后落在字母的第一位
            while paragraph[pointer2].isalpha() == False:
                pointer2+=1
                if(pointer2>len(paragraph)-1):
                    flag=1
                    break
            if flag == 1:
                break
            pointer1 = pointer2
        maxCountWord = ""
        maxCount = -1
        for key in map.keys():
                if map[key] > maxCount and key not in banned and not key == '':
                    maxCount = map[key]
                    maxCountWord = key
        return maxCountWord
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned=["hit"]
#paragraph = "z, j? M, Z? W. N. V. i. R. u' s' y' R. q, r' x, I. Y' v; X' h, T? L! D' X. W? W. W, s, U. e. L! n, W, t; X, p. r, e, M' V! W; r? z, V' V, j; I! o. X? w, z; g. Z' H! m, Z; g! u. x! n? Y; V' Y' q. f, p' S! Q; j! z! T! Y! k; y? m' R, u? y' Q' q! h. V! O? y? M? q' Z, R. q; X, l! i? r; J? p' d; L! J, k? z, Z; T! k, Q! y. z. w? l' t? U! F! I. y! o. T, z, N. H? L. Q. u' p! p; E? l' V' t! G, w. x? t, m; m; m. v! v? x. z' y? w; l, Z, x! P? p. E. s' x, Z, k? y; u, l' R; u? V' a. o' F' Z? n. w. F? N, G. y, g? O. n' F, M. s? S. D. Z, Y! x? u? x! U, v, x, Q! c; v! w, S, N! z? F; m? p' z' W; o. W; P! u; X' S? P' k; V? z. v. n, y. r! M; I? s; X. T' R' l. u; X. T, V. v! y; q; p. h? x! G; C? N; T? K. P' j? y, g, T, s' u. v; n, B, w, t; v? J' S! Q, Q? H, W, Q, N? H! K! U! U; s! j, X' s' B, t' z; x' u; q; r' o! U; O' W, r? p, y; k. w; s. o. v. z; y, t? U; S? t? o! x; X' L, R. o; J, U, y! I' v? z, W, W! y. u, s. e. t! Y; k; l. K? x? v? W; r? O. W; S' p; U. Z; q? P? c' y' O' T. Y' y. j, i' T' M; M! q; o."
#banned=["r","l","q","s","h","w","x","i","a","f","e","p","v","m","j","b","k","o","c","t"]     
print(Solution().mostCommonWord(paragraph, banned))

