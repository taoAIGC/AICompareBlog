# Làm cách nào để đặt thẻ Canonical? Ngừng việc nhiều trang trỏ về trang chủ, 5 tình huống này sẽ được xử lý hiệu quả hơn

> Ngôn ngữ: Tiếng Trung | Khu vực: Trung Quốc/Toàn cầu | Từ khóa: Cách thiết lập thẻ canonical, thẻ canonical, cách sử dụng canonical, thẻ canonical, SEO trang trùng lặp, tối ưu đưa trang vào, lập chỉ mục website, SEO kỹ thuật

**Từ khóa**: Cách thiết lập thẻ chuẩn, thẻ chuẩn, cách sử dụng thẻ chuẩn, thẻ chuẩn, SEO trang trùng lặp, tối ưu hóa đưa trang vào, lập chỉ mục trang web, SEO kỹ thuật, xử lý nội dung trùng lặp, chuẩn hóa URL, vấn đề đưa vào, Search Console

---

## Tại sao nhiều trang web trỏ canonical về trang chủ trước khi có vấn đề về đưa vào?

Tôi đã nhìn thấy cái bẫy này quá nhiều lần.

Quản trị viên web hơi lo lắng vì trang này không được đưa vào nên đã mở phần phụ trợ và thực hiện một số thay đổi, cuối cùng nó trở thành:

- Trang bài viết trỏ về trang chủ
- Trang danh mục trỏ đến trang chủ
- Trang tham số trỏ về trang chủ
- Ngay cả các trang sản phẩm cũng trỏ về trang chủ

Nhìn bề ngoài, nó có vẻ là "thống nhất các trọng lượng".

Nhưng hiệu quả thực tế thường là: **Các công cụ tìm kiếm sẽ ngày càng bối rối về việc bạn muốn coi trang nào là trang chính. **

Thẻ canonical ban đầu được sử dụng để thông báo cho các công cụ tìm kiếm:

**"Nội dung của các trang này rất giống nhau, trước tiên vui lòng coi trang này là phiên bản chính thức."**

Nó không phải là nút sửa chữa phổ thông, cũng không phải là công cụ để đổ lỗi cho trang chủ mỗi khi trang có vấn đề.

Vì vậy, nếu gần đây bạn đang nghiên cứu cách thiết lập thẻ chuẩn, hãy để tôi đưa ra kết luận trước:

**kinh điển Điều tôi sợ nhất không phải là không viết được mà viết bừa bãi. **

---

## Chính xác thì canonical làm gì? Đừng nhầm lẫn nó với 301 hoặc noindex.

Khi nhiều người lần đầu tiếp xúc với canonical, rất có thể họ sẽ nhầm lẫn với hai điều sau:

- **Chuyển hướng 301**
- **noindex**

Chúng không giống nhau.

### 1.chuẩn
có nghĩa là:
**Trang này có thể truy cập được, nhưng tôi muốn bạn coi trang kia là phiên bản chính hơn. **

### 2. Chuyển hướng 301
có nghĩa là:
**Trang này đã được chuyển đi, bạn có thể vào thẳng địa chỉ mới. **

### 3. noindex
có nghĩa là:
**Bạn có thể thu thập dữ liệu trang này nhưng không đưa nó vào chỉ mục. **

Vì vậy canonical không phải là "xóa trang", cũng không phải là "buộc phải chuyển sang trang".

Nó giống một "ghi chú lưu trữ" hơn.

Bạn đang nói với công cụ tìm kiếm:

> Nội dung của các trang này gần như giống nhau. Phiên bản chính cần được thu thập là trang này.

Nếu bạn thậm chí không hiểu tiền đề này, nó sẽ dễ dàng trở nên khó hiểu hơn về sau.

---

## Làm cách nào để đặt nhãn chuẩn? Tôi khuyên bạn nên xem xét 5 tình huống phổ biến này trước tiên

### 1. Cùng một trang chỉ có các thông số khác nhau. Đây là cách thích hợp nhất để thêm canonical.

Đây là cách sử dụng phổ biến và tiêu chuẩn nhất.

Ví dụ: trên cùng một trang, các địa chỉ này có thể xuất hiện do thông số thống kê, thông số quảng cáo và thông số chia sẻ:

- `/seo-công cụ`
- `/seo-tools?utm_source=x`
- `/seo-tools?from=twitter`
- `/seo-tools?session=123`

Nội dung người dùng nhìn thấy gần như giống nhau, chỉ khác URL.

Cách tiếp cận ổn định nhất vào thời điểm này thường là:

**Tất cả các trang tham số đều quay trở lại URL chính. **

Tức là thống nhất chỉ điểm:

`/seo-công cụ`

Trong trường hợp này, công cụ tìm kiếm sẽ dễ hiểu hơn và ít gây rắc rối nhất.

---

### 2. Trang sắp xếp, trang lọc và trang danh sách gốc có tính lặp lại cao. Bạn có thể xem xét quay lại trang danh sách chính theo kiểu chuẩn.

Các trang thương mại điện tử, trang danh mục công cụ và trang nội dung thường có các trang như thế này:

- Sắp xếp theo giá
- Sắp xếp theo mới nhất
- Lọc theo màu sắc
- Lọc theo khu vực

Vấn đề là:
Một số trang lọc thực tế không mang lại giá trị tìm kiếm mới mà chỉ thay đổi thứ tự hiển thị của cùng một nội dung.

Ví dụ:

- `/plugin`
- `/plugins?sort=mới nhất`
- `/plugins?sort=popular`

Nếu nội dung cốt lõi của các trang tương tự nhau và không có sự khác biệt rõ ràng về giá trị tìm kiếm thì bạn có thể xem xét chuẩn hóa trang sắp xếp thành trang danh sách chính.

Nhưng đây là điều cần lưu ý:

**Không phải tất cả các trang lọc đều phải được chuẩn hóa lại. **

Nếu bản thân một trang bộ lọc có nhu cầu tìm kiếm rõ ràng, chẳng hạn như "plugin SEO phù hợp với các trang web độc lập" hoặc "plugin AI miễn phí", thì trang đó có thể tồn tại riêng thay vì được hợp nhất.

Vì thế đừng làm điều đó một cách máy móc. Trước tiên hãy kiểm tra xem trang này có giá trị độc lập hay không.

---

### 3. Nếu có nhiều URL cho cùng một nội dung thì chỉ được giữ lại một phiên bản chính một cách rõ ràng.

Vấn đề này đặc biệt phổ biến trong blog, CMS và các trang web sửa đổi.

Ví dụ: cùng một bài viết có thể xuất hiện đồng thời trong:

- liên kết mới
- liên kết cũ
- Liên kết với đường dẫn danh mục
- Liên kết không có đường dẫn danh mục
- Hai phiên bản có và không có dấu gạch chéo

Nội dung rõ ràng là một bài viết nhưng có nhiều URL.

Nếu điều này không được thực hiện, công cụ tìm kiếm sẽ phải đoán:
Trang nào là trang chính thức?

Điều quan trọng nhất bạn nên làm là trước tiên hãy chọn một URL mà bạn thực sự muốn giữ lâu, sau đó:

- Hãy cố gắng hết sức tới 301 nếu có thể 301
- Tạm thời không thể nhảy được, ít nhất bản canonical được thống nhất với bản chính.

Đừng sử dụng A hôm nay, B ngày mai và C vài tuần sau.

** Kinh điển Loại chuyện này sợ nhất chính mình bất ổn. **

---

### 4. Không nên kết hợp các trang sản phẩm và trang đích tương tự thành một chỉ vì chúng “tương tự”

Có rất nhiều cạm bẫy.

Ví dụ: bạn có các trang này:

- giày chạy bộ màu đen
- giày chạy bộ màu trắng
- Giày chạy bộ nữ
- Giày chạy bộ rộng rãi

Tất cả đều trông rất giống nhau nên có người đã truy cập thẳng vào "trang chủ giày chạy bộ" của Canonical.

Kết quả là:
Trang lẽ ra có thể bao gồm các cụm từ tìm kiếm được chia nhỏ riêng biệt đã bị chính bạn chặn lại.

Tiêu chí đánh giá của riêng tôi rất đơn giản:

**Nếu khi người dùng tìm kiếm trang này, họ mong đợi thấy nội dung khác, thông tin khác và quyết định mua hàng khác, đừng nhầm lẫn. **

Canonical chỉ phù hợp hơn khi những trang này thực sự chỉ lặp lại một chút, nội dung chính gần như giống nhau và giá trị độc lập yếu.

Nếu không, bạn không tiêu chuẩn hóa mà chủ động cắt bỏ các lối vào giao thông đuôi dài.

---

### 5. Trang đã được cập nhật và trang cũ sẽ không được giữ lại nữa. Sử dụng 301; không sử dụng mui cứng chuẩn mực.

Có một tình huống mà nó rất có thể được sử dụng không chính xác:

Trang cũ đã lỗi thời và trang mới đã thay thế hoàn toàn.

Lúc này, nhiều người lười nhảy nên thêm canonical vào trang cũ để trỏ sang trang mới, tưởng rằng "gần như".

Không hoàn toàn giống nhau.

Nếu không cần giữ lại trang cũ và bạn muốn người dùng truy cập trực tiếp vào trang mới khi họ truy cập trang cũ thì cách này thường phù hợp hơn:

**Chuyển hướng 301 thay vì chỉ viết chuẩn. **

Vì tiền đề của canonical là trang cũ vẫn tồn tại nên nó chỉ báo cho công cụ tìm kiếm "vui lòng tập trung vào trang đó".

Và 301 đang thể hiện rõ ràng:

**Trang này đã chính thức được chuyển đi. **

Nhiều người lúc bình thường không để ý đến sự khác biệt này nhưng sẽ rất xấu hổ khi kiểm tra chỉ số, cân nặng sau này.

---

## Tôi nghĩ 4 lỗi kinh điển này còn có hại hơn là không viết.

### Sai lầm 1: Tất cả các trang đều trỏ về trang chủ

Đây là hình thức xử lý thô bạo phổ biến nhất.

Vấn đề là trang chủ, trang bài viết, trang sản phẩm và trang danh mục ban đầu không phải là mục đích tìm kiếm.

Khi bạn trỏ nhiều trang trở lại trang chủ, bạn đang nói với các công cụ tìm kiếm:

"Không có trang nào trong số này quan trọng, chính trang chủ mới quan trọng."

Đừng quá ngạc nhiên nếu nhiều từ đuôi dài không thể sử dụng được.

---

### Sai lầm 2: Nội dung trang khác nhau nhiều nhưng vẫn viết canonical giống nhau

kinh điển không có nghĩa là hợp nhất "các chủ đề hoàn toàn khác nhau".

Nếu chủ đề, ý định của người dùng và hướng từ khóa của hai trang đều khác nhau nhưng chúng chỉ liên quan một chút thì bạn không nên trỏ chúng một cách ngẫu nhiên.

Công cụ tìm kiếm không chỉ thấy bạn viết chuẩn và chỉ làm theo, nó cũng sẽ tự đánh giá mức độ tương đồng của nội dung.

Nếu bạn viết ngẫu nhiên thì nhiều khi sẽ không đúng ý bạn.

---

### Sai lầm thứ 3: canonical trỏ tới 404, nhảy trang, thậm chí là các trang không lập chỉ mục

Đây là một cạm bẫy cấp thấp dễ bị bỏ qua nhất trong công nghệ.

Trang mục tiêu được trỏ đến bởi trang chuẩn tốt nhất nên đáp ứng các điều kiện sau:

- Có thể mở bình thường
- Mã trạng thái bình thường
- Không phải 404
- Không phải địa chỉ sau khi nhảy nhiều cấp
- không được lập chỉ mục

Nếu không, bạn đang cung cấp cho công cụ tìm kiếm một hướng dẫn rất mơ hồ hoặc thậm chí sai.

---

### Sai lầm 4: Một bên Canonical và một bên đưa ra tín hiệu ngược lại.

Ví dụ:

- Trang tự viết kinh điển tự tham khảo
- Một URL khác đã được gửi trong sơ đồ trang web
- Hầu hết các liên kết nội bộ đều trỏ đến URL thứ ba
- hreflang, chuyển hướng, kinh điển đấu tranh lẫn nhau

Tình huống này là rắc rối nhất.

Bởi vì những gì công cụ tìm kiếm cuối cùng nhận được không phải là một kết luận rõ ràng mà là một loạt các mẹo trái ngược nhau.

**Kinh điển thực sự hiệu quả không phải là viết đúng một điểm mà là không làm suy yếu lẫn nhau trong toàn bộ tập hợp tín hiệu URL. **

---

## Nếu bây giờ bạn muốn kiểm tra canonical thì danh sách này là đủ

Khi tôi tự khắc phục sự cố, tôi thường xem xét theo thứ tự sau:

### Bước một: Trang này có giá trị tìm kiếm độc lập không?
Nếu vậy, đừng dễ dàng chuyển nó sang trang khác.

### Bước 2: Trang này có giống trang mục tiêu không?
Nếu chúng hơi giống nhau nhưng thực sự giải quyết được các vấn đề khác nhau, đừng hợp nhất chúng lại.

### Bước 3: Trang đích có ổn định, có thể truy cập và có khả năng đưa vào không?
Không trỏ tới các trang 404, liên kết chuyển hướng hoặc các trang noindex.

### Bước 4: Các tín hiệu khác trên trang web có nhất quán không?
Kiểm tra sơ đồ trang web, liên kết nội bộ, điều hướng và chuyển hướng để xem có bất kỳ xung đột nào không.

### Bước 5: Kịch bản chuẩn, đừng chỉ viết chuẩn
Trang cũ đã bị loại bỏ nên đừng để nó chết dở.

Nhìn vào 5 bước này, hầu hết các vấn đề kinh điển đều có thể được xác định chính xác.

---

## Cách tiếp cận phổ biến hơn của tôi bây giờ: làm rõ mối quan hệ URL trước, sau đó nói về URL chuẩn

Thành thật mà nói, nhiều trang web gặp vấn đề về chuẩn, không phải vì bản thân các thẻ khó mà vì cấu trúc URL không được nghĩ ra rõ ràng ngay từ đầu.

Ví dụ:

- Cùng một nội dung có thể tạo ra ba hoặc bốn loại liên kết
- Đường dẫn danh mục thay đổi thường xuyên
- Sự tồn tại của URL cũ và mới
- Quy tắc tham số khó hiểu
- Mẫu và plug-in tự động tạo ra một loạt các trang trùng lặp

Ngay cả khi bạn vá phiên bản chuẩn trên mọi trang của loại trang web này, bạn sẽ tiếp tục vá nó sau đó.

Vì vậy, bây giờ tôi thích làm điều này trước:

**Trước tiên hãy suy nghĩ rõ ràng về "trang nào nên tồn tại, trang nào không nên tồn tại và trang nào nên được hợp nhất." **

Sau khi suy nghĩ rõ ràng, canonical sẽ trở thành một công cụ tổ chức rất tiện lợi.

Nếu không, nó có thể dễ dàng được sử dụng như một công cụ chữa cháy.

---

## Viết ở cuối

Cách đặt nhãn chuẩn thực chất không bí ẩn như tưởng tượng.

Khó khăn không phải là viết code như thế nào mà là bạn có thể đánh giá rõ ràng trước tiên hay không:

- Những trang nào thực sự trùng lặp
- Những trang nào chỉ tương tự nhưng nên giữ lại
- Những trang nào nên chuẩn
- Những trang nào thực sự nên là 301

Bây giờ tôi càng ngày càng cảm thấy giá trị cốt lõi của canonical không phải là "chuyển trọng lượng", mà là:

**Hãy để công cụ tìm kiếm biết rõ hơn trang nào trên website của bạn là phiên bản chính thức. **

Chỉ cần ý tưởng này rõ ràng, nhiều vấn đề như thu thập chậm, trang trùng lặp và lập chỉ mục hỗn loạn sẽ dễ giải quyết hơn nhiều so với trước đây.

Nếu gần đây bạn đang kiểm tra việc đưa vào, đừng chỉ kiểm tra xem trang canonical có viết nó hay không.

Hơn nữa:

**Nó có được viết vào đúng trang không? **

---

**Tìm kiếm liên quan**: Cách thiết lập thẻ chuẩn, thẻ chuẩn, cách sử dụng thẻ chuẩn, thẻ chuẩn, SEO trang trùng lặp, tối ưu hóa đưa trang vào, lập chỉ mục trang web, SEO kỹ thuật, xử lý nội dung trùng lặp, chuẩn hóa URL, vấn đề đưa vào, Search Console
