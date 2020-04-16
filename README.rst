아리스토텔레스 사용자 문서
============================

.. contents:: On this page
   :local:

레지스트리 미리보기
-----------------------

레지스트리 미리보기는 https://user-doc-2.herokuapp.com 에서 이용할 수 있습니다. 이 사이트는 코드와 문서가 변경할 때마다 재구성됩니다.

사이트에 대한 사용자 계정은 다음 파일에서 사용할 수 있습니다 : https://github.com/aristotle-mdr/user-documentation/blob/draft/server/fixtures/test_metadata.json

스타일 가이드
-------------

* 페이지를 짧게 유지 - 한 가지 주제를 다루며, 다른 페이지에 대한 링크를 가지고 있습니다.

* 제목(및 자막)은 다음과 같은 기호로 스타일링할 수 있습니다::
* 
    헤더제목
    =========
    
    서브헤더 제목
    -------------
    
    하위 서브헤더 제목
    ++++++++++++++++++
    
    세부 하위 항목 제목(그러나 이 예는 너무 깊게 들어간 예시임)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 페이지에 제목이 여러 개일 경우, 페이지 상단에 다음과 같이 페이지 목차를 삽입한다 ::
  
      .. 컨텐츠 내용:: 이 페이지에서
         :local:
    

* 사용자가 설명서를 이해하도록 주의 상자 사용:

  - 노트 note (blue):
 
    일반 정보에 노트 사용::
 
        .. note::
           API를 사용하려면 당신의 레지스트리에 아리스토텔레스-MDR API 확장이 설치되어 있어야 합니다.
           이러한 화면에 액세스할 수 없는 경우 레지스트리 관리자에게 문의하여 설치 여부를 확인하십시오.

  - 힌트 Hints (green):

    사용자에게 명확하지는 않지만 작업을 더 빠르고 쉽게 수행할 수 있는 내용을 표시하려면 힌트를 사용하십시오.::    

        .. hint::
           윈도우즈에서는 'Alt+Q'를, 맥에서는 'Cmd+Q'를 눌러 퀵 검색 바에 접속할 수 있습니다.           

  - 주의 Attention (orange):
    
    주의 상자를 사용하여 스크린샷이 사용자 화면과 다르게 보이는 이유를 설명하기 위기 위해서는 주의를 사용하십시요.
    이건 다음을 포함합니다
    
    예를 들어::
   
   
       .. attention:: 화면에 편집 링크가 표시되지 않으면 이 메타데이터를 편집할 수 있는 권한이 없을 수 있습니다.
       
  - 경고 Warning (red):

    사용자가 원하지 않거나 취소할 수 없는 작업을 수행하려는 경우, 예를 들어 삭제나 비공개 공개해야 하는 작업 등등
    이렇게 합니다 ::
        
       .. warning:: 핀집 링크가 화면에 표시되지 않으면 이 메타데이터를 편집할 수 있는 권한이 없을 것입니다.       

링크 삽입하기
---------------


문서의 다른 부분과 연결된 링크
++++++++++++++++++++++++++++

다른 섹션에 대한 링크는 ``:doc`` 지시문으로 측면 텍스트에 추가할 수 있습니다::
 
   자세한 내용은 챕터 :doc:`/user_help/index` 장을 참조하십시오   

user_help/index.rst" 파일이 존재하면, 링크를 추가와 해당 페이지 제목 텍스트가 추가된다. 이것은 제목이 바뀌면 링크도 바뀐다는 것을 의미한다.

만약 링크에 대한 사용자 정의 텍스트가 필요한 경우, 사용자 정의 텍스트와의 링크 주위에 꺽쇠기호(``<``  와 ``>``)를 먼저 사용하십시오.::


    :doc:`사용자 정의 텍스트 my custom text </user_help/index>`
 
외부 웹페이지 링크 하기
++++++++++++++++++++++

외부 페이지에 대한 링크가 필요할 때, 우리는 문서의 인쇄 버전을 만들 때 이 형식의 링크가 각주와 함께 더 쉽게 표시될 수 있는 것처럼 외부하이퍼링크 `External hyperlinks`_ 를 사용합니다.

* 만약 링크 텍스트가 단일 단어일 경우, 밑줄 직선을 추가하면 그 것은 링크가 링크가 됩니다: ``link_``. 
* If the link text is multiple words, add backticks around the words, anding an underscore makes it a link: ```a longer link`_``.
* 만일 링크 텍스트가 여러 단어일 경우, 단어 주위에 백틱을 추가하고 밑줄을 그으면 그 것은 링크 길이가 더 긴 링크가 됩니다: ```a longer link`_``.

예 제 ::

      Python_ 또는 'Aristotle Metadata Registry' 같은 외부 하이퍼링크(External Hyperlinks).


      .. _Python: http://www.python.org/
      .. _Aristotle Metadata Registry: http://www.aristotlemetadata.com

.. _External Hyperlinks: http://docutils.sourceforge.net/docs/user/rst/quickref.html#external-hyperlink-targets


이미지 추가하기
-------------

일반 이미지 포함 방법
++++++++++++++++++++

스핑크스와 RST는 다음과 같은 지시를 사용하여 이미지를 삽입할 수 있도록 합니다.::

       .. image:: /_static/aristotle_square_small.png
          :alt: The Aristotle-MDR logo
          :align: right

    이미지 경로(첫 번째 이름 없는 전달인자)는 docs 디렉토리(`docs directory`_)에 상대적이어야 하며, 대부분의 이미지는 ``_static`` 디렉토리 아래에 있을 것입니다.

.. _docs directory: https://github.com/aristotle-mdr/user-documentation/tree/draft/docs

스크린샷 포함 방법
+++++++++++++++++

스크린샷이 필요한 지점마다 다음과 같은 스크린샷 지시어를 삽입하십시오::

    .. screenshot::
       :server_path: /        <- 문서에 삽입할 페이지의 URL
       :alt: alternate text   <- 삽입된 이미지의 alt 태그
       :login: {'url': '/login', "username": "vicky", "password": "Viewer"}
       :alt: alternate text   <- 삽입된 이미지의 alt 태그

문서가 작성되면, 스크린샷은 테스트 서버에서 생성될 것입니다.
항상 이미지 및 스크린샷을 설명하는 짧은 alt 태그를 포함하십시오.

로그인할 사용자가 필요한 페이지의 경우 ``:login:`` 인자를 삽입하십시오.

원형 'clicker'를 링크 위에 위치하려면 다음과 같이 하십시오::

    .. screenshot::
       :server_path: /
       :clicker: a[href="/account/roles"]

그렇지않고,사용 가능한 클래스를 가지고 있는 경우는 다음과 같이 하십시오::
       :clicker: div.row

또는 ID가 있는 경우 다음과 같이 하십시오::

       :clicker: div#content

스크린샷을 자르거나 마크를 만드는 방법에 대한 자세한 내용은 다음 사이트를 참조하십시오 : https://github.com/LegoStormtroopr/sphinx-selenium-screenshots/


RAW HTML 삽입
-------------

가능한 곳에 모든 도움말 텍스트는 RST 형식이어야 하지만 콘텐츠를 마이그레이션할 때 일부 경우 일반 html에 붙여넣기가 더 쉽다면 다음과 같이 할 수 있습니다::

    .. raw:: html
        <p> 이 곳은 문단 내에서 <b>볼드 텍스트</b>로 렌더링 될것입니다!!</p>

초안 및 게시 지점(Branch)
-----------------

우리는 두 개의 주요 지점(Main Brandh)을 가지고 있습니다:

1. 초안 - 이것은 작업 부서로, 콘텐츠의 미완성된 복사본이 있을 수 있고, 프리뷰가 준비되면 https://aristotle-mdr.github.io/user-documentation/ 에서 확인할 수 있습니다

2. 퍼블리싱 - 이것은 최종 문서 분기 지점으로, 퍼블리싱될 때 https://aristotle-mdr.github.io/published-documentation/에서 이용할 수 있습니다

모든 작업은 초안으로 진행되며, 새로운 버전의 문서로 배포할 준비가 되면 퍼블리싱으로 풀링(pull)합니다.

문제 해결 페이지
----------------

만약 페이지가 업데이트 되지 않으면, 퍼블리싱도구 `publishing tool`_ 를 검토하십시오, 가장 최근 빌드를 표시가 되고 많은 녹색 체크틱(green ticks)이 있어야 합니다. 만약 빨간 표시가 있다면 그 빌드는 실패한 것입니다. 
페이지 하단으로 건너 뛰게 되고 당신에게 어떻게 실패했는지, 왜 실패했는지 표시할 것입니다. -

우리는 오류가 있는 페이지나 제대로 렌더링되지 않는 페이지를 디버깅하는 데 도움이 되도록 RST와 HTML을 나란히 보여주는 라이브 업데이트 편집기 `live updating editor`_ 가 있습니다.

모든 변경사항과 함께 재빌드되는 '문서화를 위한 전용 서버' `server specifically for documentation purposes`_ 가 있습니다. 
로그인을 위한 사용자 및 인증 정보는 "서버 테스팅고정정보"`server fixtures`_ 에 있다.

.. _퍼블리싱 도구: https://travis-ci.org/aristotle-mdr/user-documentation/
.. _라이브 업데이트 편집기: https://aristotle-user-doc.herokuapp.com/fafl/
.. _문서화를 위한 전용 서버: https://aristotle-user-doc.herokuapp.com
.. _서버 테스팅고정정보: https://github.com/aristotle-mdr/user-documentation/blob/draft/server/fixtures/test_metadata.json

용어집
-------

만약 용어가 현재 없는 경우 이슈를 추가할 수 있습니다.

Argument 
    (전달)인자. 지시어가 받아들일 수 있는 추가 정보. 인자는 선택적이거나 필수적일 수 있음::
    
      .. image: 이미지이름(.)확장자, image_name.png
         :alt: alt 태그는 명명된 전달 인자임. 그러나 image_name.png는 이름없는 인자임.
         

Directive
    지시어. 두 점(dot) 뒤에 오는 명령어 - ``.. image:``

RST
    RST텍스트형식. 재구성텍스트 - 문서를 작성하는 데 사용하는 텍스트 형식
    

