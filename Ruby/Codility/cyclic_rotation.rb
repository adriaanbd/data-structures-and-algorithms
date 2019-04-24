# CODILITY
# ROTATING ARRAY
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(a, k)
    k.times { a.unshift(a.pop) } unless a.all? { |i| i == i[0] } || a.length == k
    a
end

# Other version:

# def solution(a, k)
#     return a if a.all? { |i| i == i[0] } || a.length == k
#
#     k.times do
#         a.unshift(a.pop)
#     end
#     a
# end

