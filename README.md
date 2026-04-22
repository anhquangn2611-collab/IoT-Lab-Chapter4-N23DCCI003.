# IoT Lab — Chapter 4: Raspberry Pi with Python

![GitHub Actions](https://github.com/anhquangn2611-collab/IoT-Lab-Chapter4-N23DCCI003/actions/workflows/ci.yml/badge.svg)
![GitLab CI](https://gitlab.com/anhnguyenquang95/iot-lab-chapter4-n23dcci003/badges/main/pipeline.svg)

---

## Thông tin sinh viên
* **Họ tên:** Nguyễn Quang Anh
* **MSSV:** N23DCCI003
* **Lớp:** D23CQCI01-N

---

## Giới thiệu bài tập
Bài Lab này tập trung vào việc sử dụng Python để giám sát hệ thống và mô phỏng cảm biến trên nền tảng Raspberry Pi (thông qua QEMU), đồng thời thiết lập luồng CI/CD song song trên cả GitHub và GitLab.

### Các bài tập đã hoàn thành:
1. **BT1:** Giám sát thông số hệ thống (CPU, RAM, Disk) qua QEMU.
2. **BT2:** Mô phỏng dữ liệu cảm biến và cảnh báo.
3. **BT3:** Lập trình điều khiển GPIO (Wokwi).
4. **BT4:** Hiển thị thông tin lên Sense HAT.
5. **BT5:** Tích hợp hệ thống tổng thể.
6. **BT6:** Cấu hình Multi-remote Git và Pipeline CI/CD.

---

## Hướng dẫn chạy Pipeline
Mỗi khi thực hiện thay đổi code, chỉ cần thực hiện lệnh sau để cập nhật cả 2 nền tảng:
```bash
git add .
git commit -m "Your message"
git push origin main