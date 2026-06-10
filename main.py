# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 21009 문가은
# 프로젝트 주제: 가구 배치 프로그램

# ==========================================
# [수행평가] 가구 배치 도우미 - main.py
# ==========================================

# 1. 가구 도감 데이터 (2차원 리스트)
furniture_list = [
    [1, "침대", 3, 2],
    [2, "책상", 2, 2],
    [3, "옷장", 2, 1]
]

# 2. 방 생성 함수
def create_room(w, h):
    return [[0] * w for _ in range(h)]

# 3. 방 출력 함수
def display_room(room):
    print("\n--- 🏠 현재 방 배치 상태 ---")
    for row in room:
        print(row)
    print("-------------------------\n")

# 4. 가구 배치 및 검사 함수 (업그레이드 버전)
def check_and_place(room, f_w, f_h, rotate, start_x, start_y):
    room_h = len(room)     # 방의 세로 크기
    room_w = len(room[0])  # 방의 가로 크기
    
    # [회전 처리]
    if rotate == 'Y' or rotate == 'y':
        f_w, f_h = f_h, f_w
        print(f"🔄 가구가 회전되었습니다. (가로: {f_w}, 세로: {f_h})")
        
    # 🚨 [1단계 검사: 방의 범위를 벗어나는지 체크]
    if (start_x + f_w > room_w) or (start_y + f_h > room_h):
        print("❌ [경고] 가구가 방의 범위를 벗어나 배치할 수 없습니다!")
        return False

    # 🚨 [2단계 검사: 이미 다른 가구와 겹치는지 체크]
    for y in range(start_y, start_y + f_h):
        for x in range(start_x, start_x + f_w):
            if room[y][x] != 0:
                print("❌ [경고] 이미 그 자리에 다른 가구가 있어서 겹칩니다!")
                return False

    # 🎉 [3단계 실행: 실제 가구 배치하기]
    for y in range(start_y, start_y + f_h):
        for x in range(start_x, start_x + f_w):
            room[y][x] = 1
            
    return True

# ==========================================
# 5. 메인 실행 흐름 (반복문 활용)
# ==========================================
print("🏠 나만의 인테리어 가구 레이아웃 프로그램 🏠")
room_w = int(input("방의 가로 크기를 입력하세요 (예: 5): "))
room_h = int(input("방의 세로 크기를 입력하세요 (예: 5): "))

my_room = create_room(room_w, room_h)
display_room(my_room)

while True:
    print("----------------------------------------")
    action = input("가구를 배치하려면 '추가', 끝내려면 '종료'를 입력하세요: ")
    
    if action == "종료":
        print("🎉 인테리어가 완료되었습니다! 프로그램을 종료합니다.")
        break
        
    elif action == "추가":
        print("\n--- 🛋️ 가구 도감 목록 ---")
        for item in furniture_list:
            print(f"번호: {item[0]} | 이름: {item[1]} | 크기: {item[2]}x{item[3]}")
            
        choice = int(input("배치할 가구 번호를 선택하세요: "))
        
        selected_furniture = None
        for item in furniture_list:
            if item[0] == choice:
                selected_furniture = item
                break
                
        if selected_furniture is None:
            print("❌ 잘못된 가구 번호입니다. 다시 선택해 주세요.")
            continue
            
        f_name = selected_furniture[1]
        f_w = selected_furniture[2]
        f_h = selected_furniture[3]
        
        rotate = input(f"{f_name}을 회전하시겠습니까? (Y/N): ")
        start_x = int(input("배치할 X 좌표를 입력하세요 (0부터 시작): "))
        start_y = int(input("배치할 Y 좌표를 입력하세요 (0부터 시작): "))
        
        success = check_and_place(my_room, f_w, f_h, rotate, start_x, start_y)
        
        if success:
            print(f"✅ {f_name} 배치 성공!")
        
        display_room(my_room)