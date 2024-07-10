from bisect import bisect_right

n = int(input())
jobs = []

for _ in range(n):
    s,e,p = map(int,input().split())
    jobs.append((s,e,p))

# 끝나는 시간을 기준으로 정렬
jobs.sort(key=lambda x: x[1])
    
# DP 배열 초기화
dp = [0] * (n + 1)
end_times = [job[1] for job in jobs]  # 끝나는 시간만 저장하는 리스트
    
for i in range(1, n + 1):
    s, e, p = jobs[i - 1]
        
    # 현재 알바 선택하지 않는 경우
    dp[i] = dp[i - 1]
        
    # 현재 알바와 겹치지 않는 마지막 알바 찾기
    idx = bisect_right(end_times, s - 1)
        
    # 겹치지 않는 알바의 인덱스는 idx - 1
    dp[i] = max(dp[i], dp[idx] + p)

print(dp[n])