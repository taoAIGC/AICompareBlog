# Làm cách nào để viết robots.txt? Đừng chỉ từ chối nhiều người trong số họ ngay từ đầu. Sẽ hiệu quả hơn nếu bạn làm rõ 5 quy tắc này trước.

> Ngôn ngữ: Tiếng Việt | Khu vực: Toàn cầu | Từ khóa: cách viết robots.txt, cài đặt robots.txt, quy tắc robots.txt, Disallow, Allow, kiểm soát thu thập dữ liệu, SEO kỹ thuật, tối ưu thu thập dữ liệu website

**Từ khóa**: Cách viết robots.txt, cài đặt robots.txt, quy tắc robots.txt, Không cho phép, Cho phép, kiểm soát thu thập dữ liệu, SEO kỹ thuật, tối ưu hóa thu thập dữ liệu trang web, thu thập thông tin của công cụ tìm kiếm, đưa trang, ngân sách thu thập dữ liệu, noindex, Search Console, chỉ mục trang web

---

## Tại sao nhiều người thay đổi robots.txt của họ và trang đầu tiên họ chặn là trang quan trọng nhất của họ?

Nhiều người lần đầu tiên gặp robots.txt và có những suy nghĩ tương tự trong đầu:

- Không muốn công cụ tìm kiếm thu thập dữ liệu
- Tôi muốn chặn “các trang vô dụng” trước
- Tôi cảm thấy rằng các quy định càng chặt chẽ thì sẽ càng an toàn hơn
- Ngay khi có vấn đề với việc đưa trang vào, tôi muốn thay đổi nó trong robots.txt.

Sau đó, kết quả phổ biến nhất là:

- Thư mục kiểm tra không bị chặn
- Thay vào đó, thư mục bài viết chính thức đã bị chặn
- Tài nguyên CSS và JS bị chặn cùng nhau
- Sơ đồ trang web đã được viết nhưng lại bị kẹt bởi các quy tắc của robot.

Có vẻ như bạn đang làm SEO kỹ thuật nhưng thực chất bạn đang tự chuốc lấy rắc rối trong nhiều trường hợp.

Vì nếu robots.txt viết sai sẽ không ảnh hưởng đến một bài viết nào đó mà có thể ảnh hưởng đến cả một loạt trang.

Vì vậy, bây giờ khi tôi xem cách viết robots.txt, trước tiên tôi sẽ không hỏi “những gì khác có thể bị chặn”, mà trước tiên hãy hỏi:

**Tôi có muốn kiểm soát việc thu thập dữ liệu hay tôi chỉ lo lắng và muốn thay đổi điều gì đó trước tiên?**

Hai điểm xuất phát này có vẻ giống nhau nhưng kết quả cuối cùng lại rất khác nhau.

---

## Chính xác thì robots.txt làm gì? Đừng hiểu lầm “không thu thập dữ liệu” là “không bao gồm”

Đây là bước khó hiểu nhất.

Nhiều người cho rằng chỉ cần `Disallow` được viết bằng robots.txt thì trang này chắc chắn sẽ không xuất hiện trong kết quả tìm kiếm.

Điều đó không hoàn toàn đúng.

robots.txt chủ yếu giải quyết:

**Bạn có cho phép công cụ tìm kiếm thu thập thông tin trên đường dẫn này không.**

Nó gần với "quy tắc thu thập dữ liệu" hơn là "bao gồm chuyển đổi".

Trước tiên bạn có thể tách các khái niệm này:

### 1. robots.txt
có nghĩa là:
**Chưa bắt được đường này hoặc bắt theo quy định của tôi.**

### 2. noindex
có nghĩa là:
**Trang này có thể được thu thập thông tin nhưng tôi không muốn nó được lập chỉ mục.**

### 3. sơ đồ trang web
có nghĩa là:
**Những URL này là các trang chính thức mà tôi muốn bạn khám phá và tìm hiểu trước tiên.**

### 4. chuẩn
có nghĩa là:
**Nội dung của các trang này rất giống nhau, vui lòng sử dụng một trong số chúng làm phiên bản chính trước.**

Bạn sẽ thấy rằng mỗi công cụ này đều có mục đích riêng.

Vì vậy nếu bạn coi robots.txt như một “nút ẩn phổ quát” thì sau này sẽ dễ thực hiện các thay đổi và trở nên lộn xộn hơn.

Một tình huống đặc biệt là đặc biệt phổ biến:

**Trang này đã được phát hiện bởi các liên kết bên ngoài. Mặc dù bạn không cho phép thu thập dữ liệu nhưng nó vẫn có thể xuất hiện trong chỉ mục dưới dạng URL.**

Vì vậy, đừng đánh đồng robots.txt với “hoàn toàn không được bao gồm”.

---

## Làm cách nào để viết robots.txt? Tôi muốn đề nghị làm rõ 5 quy tắc này trước

### 1. Chặn các trang chức năng thực sự không cần thiết để chụp trước. Đừng chặn thư mục nội dung ngay khi bạn bắt đầu.

Robots.txt là cách phù hợp nhất để xử lý, thường là các đường dẫn sau:

- Thư mục phụ trợ
- Trang đăng nhập
- Giỏ hàng, trang thanh toán
- Trang kết quả tìm kiếm trang web
- Các trang tham số trùng lặp rõ ràng
- Đường dẫn chức năng mà bạn không muốn bị vướng vào môi trường thử nghiệm

Điểm chung của những trang này là rõ ràng:

**Chúng thường không tồn tại để có được lưu lượng tìm kiếm.**

Vì vậy, bạn có thể ưu tiên hạn chế việc thu thập dữ liệu các trang đó.

Nhưng sai lầm phổ biến nhất mà nhiều người mắc phải là chặn các thư mục bài viết, thư mục danh mục và thư mục sản phẩm ngay khi bắt đầu vì nghĩ rằng họ nên "thận trọng trước tiên".

Điều này rất nguy hiểm.

Bởi vì những gì công cụ tìm kiếm thực sự cần nắm bắt thường là những trang nội dung trang trọng này.

Nếu sau này bạn chặn ngay cả nội dung chính và nói về việc đưa vào, xếp hạng và phân phối liên kết nội bộ thì phần lớn nội dung đó sẽ trở nên vô ích.

---

### 2. Không chặn tài nguyên CSS, JS và hình ảnh, nếu không trang thậm chí có thể không hiển thị bình thường.

Cái bẫy này thực sự không phải là hiếm.

Khi ai đó nhìn thấy các thư mục này `/assets/`, `/static/`, `/wp-content/`, `/js/`, phản ứng đầu tiên của họ là:

"Đây không phải là văn bản chính, xin hãy dừng chúng lại trước."

Nhưng vấn đề là khi các công cụ tìm kiếm hiện thu thập dữ liệu các trang, chúng không chỉ xem văn bản HTML mà còn xem liệu trang có thể được hiển thị bình thường hay không, bố cục đã hoàn chỉnh chưa và trải nghiệm trên thiết bị di động có bình thường hay không.

Nếu bạn chặn các tài nguyên chính, loại sự cố này có thể xảy ra sau đó:

- Trang có thể được thu thập thông tin nhưng kết xuất không đầy đủ.
- Văn phong khó hiểu, vị trí các nội dung quan trọng bị bóp méo.
- Đánh giá trải nghiệm di động bị ảnh hưởng
- Bạn cho rằng nội dung trang có vấn đề nhưng thực chất là do tài nguyên chưa được giải phóng

Vì vậy, robots.txt không "chặn tên thư mục nếu nó không giống văn bản".

Một cách tiếp cận ổn định hơn là:

**Trước tiên hãy xác nhận xem các tài nguyên trong thư mục này có ảnh hưởng đến hiển thị bình thường của trang hay không, sau đó quyết định xem có chặn chúng hay không.**

Đặc biệt với những website phụ thuộc nhiều vào front-end, đừng cố gắng tránh rắc rối ở bước này.

---

### 3. Nếu bạn muốn ngăn việc lập chỉ mục trang, đừng chỉ dựa vào robots.txt. Bạn phải phân biệt giữa nó và noindex.

Quá nhiều người sử dụng điều này một cách khó hiểu.

Ví dụ: nếu bạn không muốn một số trang xuất hiện trong kết quả tìm kiếm, ý tưởng đúng thường không phải là kiểm tra robots.txt trước mà hãy xem:

- Trang này có nên được thu thập thông tin nhưng không được đưa vào?
- Có nên chuyển trang 301 này sang trang khác không?
- Trang này có nên chuẩn hóa thành phiên bản chính thức không?
- Trang này không nên tồn tại công khai ngay từ đầu phải không?

Nếu bạn chỉ muốn ngăn việc lập chỉ mục trang, trong nhiều trường hợp, bạn nên ưu tiên những việc sau:

- `noindex`
- kinh điển
- Mã trạng thái trang
- Chuyển hướng

Thay vì đặt robots.txt lên trên nó.

Bởi vì khi bạn tắt hoàn toàn tính năng thu thập thông tin, các công cụ tìm kiếm có thể không nhận được tín hiệu noindex trên trang của bạn.

Logic này có thể khiến nhiều người bối rối khi lần đầu tiên nghe nó, nhưng nó đặc biệt quan trọng.

**robots.txt giải quyết vấn đề "có bắt giữ hay không" chứ không phải "làm thế nào để thu thập sau khi bắt giữ".**

---

### 4. Đừng chỉ sử dụng Disallow làm quy tắc. Một số thư mục cần được phát hành một phần.

Nhiều người viết robots.txt và biết một hành động:

`Không cho phép`

Trên thực tế, điều mà nhiều trang web thực sự cần là:

**Việc thu thập thông tin của các thư mục lớn bị hạn chế nhưng các đường dẫn riêng lẻ phải được giải phóng.**

`Cho phép` sẽ được sử dụng tại thời điểm này.

Ví dụ: hầu hết có các trang tham số vô giá trị trong một thư mục, nhưng có một số tài nguyên tĩnh, trang cốt lõi hoặc các tệp cần thiết cần được nắm bắt. Lúc này, nếu chỉ phong tỏa toàn bộ đoạn đường thì đặc biệt dễ gây ra hư hỏng do tai nạn.

Thói quen của riêng tôi là:

- Viết những quy tắc lớn mà bạn muốn bảo vệ trước tiên
- Bổ sung con đường mỏng cần phải được dọn sạch
- Cuối cùng lấy một vài URL thật để test

Không phải là ít quy tắc hơn có nghĩa là quy tắc nâng cao hơn, nhưng:

**Liệu quy tắc của bạn có thể giúp "dừng cái gì nên dừng và để cái gì nên buông" hay không.**

Nếu bạn chỉ cố gắng giải quyết rắc rối, thường thì kết quả cuối cùng không phải là "sạch hơn" mà là "mờ".

---

### 5. Đừng vội lên mạng sau khi thực hiện thay đổi. Hãy kiểm tra trước, sau đó kiểm tra Search Console và phản hồi thu thập dữ liệu thực tế.

Đây là một bước mà tôi đặc biệt coi trọng hiện nay.

Nhiều vấn đề với robots.txt không phải do không thể viết mà là do thiếu xác minh sau khi viết.

Tôi thường làm ít nhất vài điều sau:

- Chọn một vài URL trang bài viết để xem có bị chặn nhầm hay không.
- Chọn một số trang danh mục, trang thông số và trang chức năng để kiểm tra riêng
- Kiểm tra xem URL trong sơ đồ trang web có xung đột với robot không
- Kiểm tra xem dòng chữ "Đã gửi nhưng bị chặn bởi robots.txt" có xuất hiện trong Search Console hay không
- Nếu bạn có thể đọc nhật ký, bạn có thể biết gần đây công cụ tìm kiếm đã thu thập dữ liệu gì.

Bạn sẽ thấy rằng nhiều quy tắc đều ổn chỉ bằng cách nhìn vào văn bản, nhưng URL thực sự sẽ được tiết lộ.

Vì vậy, đừng nghĩ robots.txt là một tệp "hoàn thành và tải nó lên".

Nó giống như một cái van nhỏ cần được kiểm tra mọi lúc.

---

## Về cơ bản bây giờ tôi sẽ tránh các phương pháp viết robots.txt này.

- `Không cho phép: /` ngay khi nó xuất hiện
- Trang web chính thức vẫn giữ nguyên các quy tắc đánh chặn từ thời kỳ môi trường thử nghiệm
- Chặn tất cả các thư mục CSS, JS và hình ảnh
- Nghĩ rằng “không bò” có nghĩa là “sẽ không bao giờ được đưa vào”
- Sơ đồ trang web đã gửi A, nhưng robot đã chặn thư mục chứa A.
- Nhiều môi trường chia sẻ một bản sao của robots.txt, dẫn đến xung đột giữa quy tắc trực tuyến và quy tắc kiểm tra

Phần rắc rối nhất của những vấn đề này là:

**Bề ngoài bạn có thể không nhất thiết gặp phải lỗi ngay lập tức, nhưng lưu lượng truy cập, kết xuất, thu thập thông tin và đưa vào sẽ dần dần trở nên kỳ lạ cùng nhau.**

Và loại vấn đề này thường không rơi ra một bài viết mà là một đoạn.

---

## Nếu bạn muốn kiểm tra robots.txt ngay bây giờ, bạn có thể thực hiện trực tiếp 5 bước sau

### Bước 1: Trước tiên hãy liệt kê các loại trang bạn thực sự muốn được thu thập thông tin
Ví dụ: trang bài viết, trang sản phẩm, trang danh mục và trang chủ đề cốt lõi.

### Bước 2: Liệt kê các đường dẫn bạn không muốn lãng phí ngân sách thu thập dữ liệu của mình
Ví dụ: phụ trợ, đăng nhập, giỏ hàng, trang kết quả tìm kiếm, thư mục kiểm tra, trang tham số trùng lặp rõ ràng.

### Bước 3: Kiểm tra xem thư mục tài nguyên có bị vô tình làm hỏng không
Tập trung vào CSS, JS, hình ảnh và các tài nguyên phụ thuộc vào giao diện.

### Bước 4: Đặt robots, sitemap, canonical và noindex lại với nhau.
Đừng để những tín hiệu này xung đột với nhau.

### Bước 5: Kiểm tra bằng URL thực trước khi lên mạng và tiếp tục đọc phản hồi sau khi thực hiện thay đổi
Đặc biệt chú ý đến lời nhắc chặn và ngoại lệ thu thập dữ liệu của Search Console.

Quá trình này không phức tạp nhưng nó thực sự có thể giúp bạn tránh được rất nhiều cạm bẫy ở mức độ thấp.

---

## Phương pháp phổ biến nhất của tôi hiện nay là để AI thực hiện kiểm tra quy tắc cho tôi trước, sau đó so sánh quy tắc nào có nhiều khả năng vô tình làm hỏng trang nhất.

Điều rắc rối nhất đối với các tệp như robots.txt không phải là chúng dài mà là chúng mỏng.

Đôi khi một quy tắc tưởng chừng như ổn nhưng khi đưa vào cấu trúc của toàn bộ trang web lại bắt đầu gây ra những thiệt hại vô tình.

Vì vậy khi kiểm tra bây giờ, trước tiên tôi sẽ liệt kê thông tin này cho AI:

- Cấu trúc thư mục chính của website
- Những trang nào bạn muốn thu thập dữ liệu và những trang nào bạn không muốn thu thập dữ liệu?
- Quy tắc robots.txt hiện tại
- Tình trạng cơ bản của sitemap, canonical và noindex

Sau đó, hãy để tôi xem xét các mô hình khác nhau một cách riêng biệt:

- Quy tắc nào có nhiều khả năng chặn nhầm nội dung chính thức nhất?
- Những thư mục nào không nên bị chặn?
- Những nơi nào tưởng chừng như không rắc rối nhưng sẽ tạo ra cạm bẫy cho việc đưa vào sau này?

Nếu muốn nhanh chóng nhận thấy sự khác biệt trong nhận định giữa các mô hình khác nhau, đôi khi tôi sẽ trực tiếp sử dụng **So sánh AI** và xem xét các đề xuất do Claude, GPT và DeepSeek đưa ra.

Thay vì để nó quyết định thay mình, tôi có thể nhanh chóng tìm ra những “điểm sát thương vô tình dễ bỏ sót sau khi nhìn lâu”.

Trong nhiều trường hợp, khó khăn của kiểu cấu hình kỹ thuật này không phải là bạn không biết viết mà là bạn cho rằng bài viết của mình rất ổn định nhưng thực tế nếu bỏ sót một điểm sẽ ảnh hưởng đến diện rộng. **

---

## Viết ở cuối

Làm cách nào để viết robots.txt? Bây giờ tôi càng ngày càng cảm thấy nó không đơn giản như “ngưng một chút rồi mới nói”.

Nó giống như trả lời hai câu hỏi:

1. **Nội dung nào đáng được công cụ tìm kiếm chú ý?**
2. **Những đường dẫn nào không nên tiếp tục lãng phí tài nguyên thu thập dữ liệu?**

Nếu bạn suy nghĩ rõ ràng về hai vấn đề này thì robots.txt thường sẽ không lộn xộn.

Không phải là nội dung của nhiều trang web không đủ hoặc sơ đồ trang web không được gửi mà chính các quy tắc thu thập thông tin đã chặn đường ngay từ đầu.

Vì vậy, nếu gần đây bạn đang có ý định thay đổi robots.txt, tôi khuyên bạn đừng vội viết một loạt `Disallow`.

Trước tiên, hãy xem xét các loại trang, thư mục tài nguyên, mục tiêu đưa vào và các tín hiệu kỹ thuật khác cùng nhau, sau đó quyết định trang nào sẽ bị chặn và trang nào nên được đưa vào.

Nếu robots.txt được viết chính xác, các công cụ tìm kiếm sẽ dễ dàng thu thập dữ liệu nội dung mà bạn thực sự muốn họ xem hơn;
Nếu bạn viết sai, những trang bạn muốn xem nhất có thể bị chặn trước.

---

**Tìm kiếm có liên quan**: Cách viết robots.txt, cài đặt robots.txt, quy tắc robots.txt, Không cho phép, Cho phép, kiểm soát thu thập thông tin, SEO kỹ thuật, tối ưu hóa thu thập thông tin trang web, thu thập thông tin của công cụ tìm kiếm, đưa trang, ngân sách thu thập thông tin, noindex, Search Console, chỉ mục trang web
