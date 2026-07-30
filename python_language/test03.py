
scores = [65,80,95,70,88,55]

count = 0
accept = 0
degree = 0

print("전체 학생 수:",len(scores))

print("최고점수:",max(scores))

print("최저점수:",min(scores))

avg = float(sum(scores) / len(scores))

print("평균:",round(avg,1))


for score in scores:

    if(score >= int(avg)):
        count+=1
    
    if(score >= 70):
        accept +=1
    else:
        degree += 1

print("평균 이상 학생 수:",count)

print("합격자 수:",accept)
print("낙제자 수:",degree)

persent = float(accept / len(scores)) * 100



print("합격률:",round(persent,1))

print("내림차순 점수:",sorted(scores,reverse = True))
        
        
    


