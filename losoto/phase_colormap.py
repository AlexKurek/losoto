from matplotlib.colors import ListedColormap
cm_data = [[0.6112562547547398, 0.6365730658187477, 0.1936175993332644],
 [0.6038988154989581, 0.6386295567527378, 0.19357458482369008],
 [0.596378271510428, 0.6406900920364416, 0.19353129575896938],
 [0.5886773669623598, 0.6427572054881125, 0.19348767708239847],
 [0.580777263820078, 0.644833463265124, 0.1934436720983897],
 [0.5726572902002797, 0.6469214768366843, 0.193399222167063],
 [0.5642946418401776, 0.6490239164396897, 0.19335426637771205],
 [0.5556640251196749, 0.6511435251686358, 0.19330874119705918],
 [0.5467372266186087, 0.6532831338624393, 0.19326258008787534],
 [0.5374825894667986, 0.6554456769662647, 0.19321571309281754],
 [0.5278643702077823, 0.657634209565482, 0.19316806637771824],
 [0.5178419407163531, 0.6598519258122573, 0.1931195617276461],
 [0.507368786602521, 0.6621021789937377, 0.19307011598807208],
 [0.4963912344783608, 0.6643885035252711, 0.1930196404422197],
 [0.48484681219662956, 0.6667146391936969, 0.1929680401142182],
 [0.4726621032866703, 0.6690845580259354, 0.1929152129858429],
 [0.45974989009712425, 0.6715024942186275, 0.19286104911254054],
 [0.4460052733625725, 0.6739729776376833, 0.192805429621738],
 [0.4313002793264544, 0.6765008714850738, 0.19274822557329307],
 [0.41547616244164226, 0.6790914148375674, 0.1926892966580526],
 [0.3983320682217058, 0.6817502708928165, 0.19262848970563573],
 [0.37960769506336633, 0.6844835819179043, 0.1925656369667798],
 [0.3589555344534543, 0.6872980320913887, 0.1925005541281677],
 [0.33589380894328696, 0.6902009196712976, 0.19243303800867553],
 [0.30972060012480546, 0.6932002402204336, 0.19236286387456666],
 [0.2793409636316316, 0.6963047829922993, 0.1922897822968843],
 [0.24286671394336462, 0.6995242430463116, 0.19221351545617935],
 [0.19646436112206545, 0.7028693522465881, 0.19213375277673403],
 [0.19302825509423574, 0.7020282516312168, 0.23662946251990125],
 [0.1938861160375202, 0.7008909514028221, 0.2739887042603917],
 [0.1946914527193663, 0.6998160787145995, 0.30446666366017033],
 [0.1954498454847638, 0.6987974384243677, 0.33029174938506756],
 [0.19616613168000974, 0.6978295963986295, 0.3527237399950759],
 [0.19684452678029102, 0.6969077643130588, 0.3725568428026118],
 [0.19748872258968608, 0.6960277046742508, 0.3903295268070212],
 [0.19810196743523606, 0.6951856520308789, 0.40642639341588505],
 [0.19868713210361955, 0.6943782472353902, 0.4211331187806841],
 [0.19924676440183753, 0.693602482293744, 0.43466848037234274],
 [0.19978313457589236, 0.6928556538572992, 0.4472041786371866],
 [0.20029827333345163, 0.692135323808657, 0.4588777041092081],
 [0.2007940038454531, 0.6914392857017275, 0.46980102112405014],
 [0.2012719688170927, 0.6907655360571905, 0.48006662064342204],
 [0.20173365349884576, 0.6901122497039412, 0.48975185587070796],
 [0.2021804053370687, 0.6894777585069605, 0.4989221210977764],
 [0.20261345082964116, 0.688860532941305, 0.5076332299000996],
 [0.20303391004635213, 0.6882591660673658, 0.5159332259665452],
 [0.20344280918977276, 0.6876723595393183, 0.5238637835014851],
 [0.20384109150536583, 0.6870989113407892, 0.5314613052729648],
 [0.20422962679577733, 0.6865377049921896, 0.5387577942903105],
 [0.20460921975088098, 0.685987700015329, 0.5457815535310035],
 [0.20498061726995404, 0.6854479234746308, 0.5525577533464082],
 [0.20534451492371958, 0.6849174624420067, 0.5591088958422971],
 [0.20570156268056344, 0.6843954572553181, 0.5654551981887056],
 [0.2060523700019885, 0.6838810954592968, 0.5716149115182103],
 [0.20639751039652654, 0.6833736063335024, 0.5776045881989107],
 [0.20673752550821817, 0.6828722559249665, 0.5834393073999221],
 [0.207072928804932, 0.6823763425140345, 0.5891328667177742],
 [0.20740420892275063, 0.6818851924509836, 0.5946979460042686],
 [0.20773183271517792, 0.6813981563085222, 0.6001462482913282],
 [0.20805624804966638, 0.680914605301528, 0.6054886217475363],
 [0.2083778863887774, 0.6804339279305498, 0.6107351658533876],
 [0.2086971651889773, 0.6799555268098288, 0.6158953243960428],
 [0.2090144901465265, 0.6794788156440228, 0.6209779674215933],
 [0.20933025731698163, 0.6790032163205248, 0.6259914639152743],
 [0.20964485513246672, 0.6785281560863642, 0.6309437466865638],
 [0.20995866633902227, 0.6780530647801691, 0.6358423707007261],
 [0.21027206987481412, 0.6775773720906627, 0.640694565908967],
 [0.21058544270901158, 0.6771005048136124, 0.6455072854766731],
 [0.2108991616603822, 0.6766218840791425, 0.6502872501860767],
 [0.21121360521429278, 0.6761409225207877, 0.6550409896906088],
 [0.21152915535682282, 0.6756570213566315, 0.6597748812189155],
 [0.21184619944495148, 0.6751695673513127, 0.6644951862637333],
 [0.21216513213242777, 0.6746779296255271, 0.6692080857419893],
 [0.21248635737196253, 0.6741814562768568, 0.6739197140757561],
 [0.21281029051572276, 0.6736794707722639, 0.6786361926175395],
 [0.21313736053793203, 0.6731712680682397, 0.6833636628268772],
 [0.21346801240565505, 0.6726561104093328, 0.6881083195976768],
 [0.21380270962665304, 0.6721332227493922, 0.6928764451368021],
 [0.21414193700665207, 0.6716017877321687, 0.6976744438040915],
 [0.21448620365250187, 0.6710609401586785, 0.7025088783425003],
 [0.21483604626275282, 0.6705097608576313, 0.7073865079549813],
 [0.21519203275319437, 0.6699472698618927, 0.7123143287228951],
 [0.21555476627216996, 0.6693724187779018, 0.717299616910463],
 [0.21592488966917944, 0.6687840822156322, 0.7223499757626618],
 [0.2163030904908126, 0.6681810481232981, 0.727473386482229],
 [0.2166901065906559, 0.6675620068426773, 0.7326782641678576],
 [0.21708673245518328, 0.6669255386664342, 0.7379735196137727],
 [0.21749382636612646, 0.6662700996367336, 0.743368628015223],
 [0.21791231854245835, 0.6655940052727989, 0.7488737058006677],
 [0.21834322043265447, 0.6648954118514829, 0.7544995970269],
 [0.21878763536176765, 0.6641722947862271, 0.7602579710372303],
 [0.21924677077950006, 0.6634224235519058, 0.7661614334070236],
 [0.21972195240707498, 0.66264333248068, 0.7722236526005009],
 [0.22021464064488966, 0.6618322866000907, 0.7784595052574703],
 [0.22072644968327948, 0.6609862414899652, 0.7848852436439754],
 [0.22125916985967642, 0.6601017958869148, 0.7915186895701888],
 [0.22181479393338166, 0.6591751354476563, 0.7983794600460552],
 [0.22239554811197648, 0.658201965672575, 0.8054892311685001],
 [0.22300392887220372, 0.657177431458081, 0.8128720482912372],
 [0.22364274688785696, 0.6560960200478748, 0.8205546925241817],
 [0.2243151797280981, 0.6549514432300565, 0.8285671161866969],
 [0.22502483544994628, 0.65373649339563, 0.8369429631928],
 [0.22577582981771166, 0.6524428664156029, 0.8457201947478523],
 [0.22657288069531778, 0.6510609420373207, 0.854941846564202],
 [0.22742142425387057, 0.6495795093958844, 0.864656951594563],
 [0.22832775913067627, 0.6479854209134026, 0.8749216728057041],
 [0.2292992267343147, 0.6462631517613959, 0.8858007048879646],
 [0.23034443876115246, 0.6443942333409933, 0.8973690236617404],
 [0.23147356704522737, 0.6423565165728902, 0.9097140897564355],
 [0.23269871667730507, 0.6401232020964713, 0.9229386526302852],
 [0.2340344117907815, 0.6376615463804071, 0.937164357936547],
 [0.23549823593702102, 0.6349311096656673, 0.9525364447078722],
 [0.2643196991043525, 0.6311263356152028, 0.9586797948787998],
 [0.30311161436042355, 0.6268181441232092, 0.9586559965053908],
 [0.3363196100823295, 0.62253277857867, 0.9586325313904399],
 [0.36562697172049996, 0.6182645561335053, 0.9586093650252826],
 [0.39202787075143214, 0.6140078816792128, 0.9585864644824297],
 [0.4161672224940426, 0.609757217241905, 0.9585637982165024],
 [0.43849158341900574, 0.6055070519830902, 0.9585413358808638],
 [0.4593254392750267, 0.6012518724468169, 0.9585190481575806],
 [0.47891352218886557, 0.5969861326972207, 0.958496906598615],
 [0.4974459858486047, 0.5927042239862939, 0.9584748834763576],
 [0.5150742278104036, 0.588400443579676, 0.9584529516417818],
 [0.5319212842862263, 0.584068962347907, 0.9584310843886589],
 [0.548088913912446, 0.579703790701166, 0.9584092553223512],
 [0.5636625763156032, 0.575298742405858, 0.9583874382318177],
 [0.5787150246969721, 0.5708473957700192, 0.9583656069634944],
 [0.5933089584135309, 0.5663430516193111, 0.9583437352957674],
 [0.6074990214813099, 0.5617786874037659, 0.958321796812743],
 [0.6213333357116899, 0.5571469066739241, 0.9582997647760362],
 [0.6348546962483324, 0.552439883039217, 0.9582776119932334],
 [0.6481015179949934, 0.5476492975655759, 0.9582553106816539],
 [0.6611085954828286, 0.5427662683759185, 0.9582328323259269],
 [0.6739077212154412, 0.5377812709766292, 0.9582101475278041],
 [0.6865281954793538, 0.5326840475327622, 0.9581872258464842],
 [0.6989972521703656, 0.5274635029376428, 0.9581640356275359],
 [0.7113404191880186, 0.5221075850466179, 0.9581405438183036],
 [0.7235818276291649, 0.5166031458399805, 0.9581167157674045],
 [0.7357444808632689, 0.5109357795062631, 0.9580925150056131],
 [0.7478504922579088, 0.5050896324389176, 0.9580679030050431],
 [0.7599212986117391, 0.4990471788407605, 0.9580428389130727],
 [0.7719778550844126, 0.4927889539250406, 0.958017279256918],
 [0.7840408164773479, 0.48629323443916134, 0.9579911776140774],
 [0.7961307090377839, 0.4795356532013875, 0.9579644842430862],
 [0.8082680964767436, 0.47248873021877685, 0.957937145668042],
 [0.8204737435714615, 0.46512129728311696, 0.9579091042092086],
 [0.832768780539252, 0.45739778502499656, 0.9578802974505666],
 [0.8451748713068462, 0.4492773301789544, 0.9578506576334797],
 [0.8577143888490698, 0.4407126446097467, 0.9578201109635059],
 [0.8704106009320288, 0.431648563808574, 0.9577885768148114],
 [0.8832878698741576, 0.42202015672233967, 0.957755966813426],
 [0.8963718703451408, 0.41175022356458596, 0.9577221837766293],
 [0.9096898297772216, 0.4007459208541454, 0.9576871204807952],
 [0.9232707966932849, 0.3888941102081983, 0.9576506582238359],
 [0.9371459432000642, 0.3760547859121786, 0.9576126651405844],
 [0.9513489091048991, 0.362051510362011, 0.9575729942195484],
 [0.9578417880103923, 0.3581384229434023, 0.9496127464150307],
 [0.958287722763831, 0.3623425896481432, 0.9360681720655919],
 [0.9587097044604168, 0.3662693904327641, 0.9230001281742397],
 [0.9591100797666036, 0.36995041157772224, 0.910363819031662],
 [0.9594909116362406, 0.3734126556347139, 0.8981189191653253],
 [0.959854021643637, 0.37667936218931225, 0.8862289539279741],
 [0.9602010249953575, 0.3797706562995821, 0.874660775877464],
 [0.9605333596595141, 0.38270406594307455, 0.8633841193656075],
 [0.9608523107372323, 0.38549493872440926, 0.8523712193049411],
 [0.9611590309620003, 0.38815678028255585, 0.8415964828319598],
 [0.9614545580292827, 0.3907015312449875, 0.8310362047287134],
 [0.9617398293171419, 0.39313979551892764, 0.8206683191455894],
 [0.9620156944482828, 0.3954810297297763, 0.8104721814931911],
 [0.9622829260575271, 0.39773370140251235, 0.8004283754200953],
 [0.9625422290604982, 0.39990542181913286, 0.7905185406259315],
 [0.9627942486652296, 0.4020030582243871, 0.7807252179208124],
 [0.9630395773251733, 0.4040328290873356, 0.7710317084671011],
 [0.9632787607974588, 0.40600038538178806, 0.7614219445537397],
 [0.9635123034422678, 0.40791088026967015, 0.7518803695766632],
 [0.9637406728765449, 0.40976902911769914, 0.7423918251457459],
 [0.9639643040768119, 0.4115791614198425, 0.7329414434201098],
 [0.9641836030107521, 0.413345265913854, 0.7235145428967636],
 [0.9643989498648654, 0.41507102995316913, 0.71409652594709],
 [0.9646107019252778, 0.41675987401307996, 0.7046727764135657],
 [0.964819196160363, 0.4184149820628394, 0.6952285555447283],
 [0.9650247515468432, 0.42003932841584407, 0.6857488944565187],
 [0.9652276711752233, 0.42163570157263025, 0.6762184811564685],
 [0.9654282441655945, 0.4232067254916975, 0.6666215399438113],
 [0.9656267474208061, 0.42475487865769457, 0.6569417006891185],
 [0.9658234472406629, 0.4262825112625563, 0.6471618550810229],
 [0.9660186008180142, 0.42779186077062437, 0.6372639963767818],
 [0.9662124576352923, 0.4292850661019413, 0.6272290384686008],
 [0.9664052607781638, 0.430764180637383, 0.6170366091245063],
 [0.9665972481813881, 0.4322311842240782, 0.6066648110052679],
 [0.9667886538207496, 0.4336879943387126, 0.5960899423907611],
 [0.9669797088639417, 0.4351364765492186, 0.5852861673183716],
 [0.9673068486894055, 0.43760373463479557, 0.5661632485543318],
 [0.967498107318142, 0.43903871854746646, 0.5545866294297127],
 [0.9676898676711795, 0.4404720073335562, 0.5426589242203486],
 [0.9678823626268119, 0.44190534853419294, 0.5303372881337983],
 [0.9680758286210954, 0.44334048978266716, 0.517572908517805],
 [0.9682705068242013, 0.4447791874086925, 0.5043096568937764],
 [0.9684666443661515, 0.4462232151322724, 0.49048233973900063],
 [0.9686644956254323, 0.4476743729397152, 0.47601438978330596],
 [0.9688643235951299, 0.4491344962376505, 0.46081476023337115],
 [0.9690664013426641, 0.4506054653859995, 0.44477365515661105],
 [0.9692710135809931, 0.45208921571791133, 0.427756511530304],
 [0.9694784583712951, 0.4535877481638821, 0.4095952664564896],
 [0.9696890489797704, 0.4551031406089066, 0.39007524048901865],
 [0.9699031159143402, 0.45663756012590945, 0.36891460144673643],
 [0.970121009170794, 0.4581932762463257, 0.3457305279111495],
 [0.9703431007224802, 0.4597726754500811, 0.3199797460050969],
 [0.9705697872930789, 0.4613782770830784, 0.2908448404176091],
 [0.9708014934585495, 0.4630127509414779, 0.25699023564876877],
 [0.9710386751322532, 0.46467893679965416, 0.21594088427211583],
 [0.9627309486730194, 0.47172617993227167, 0.19647982669867325],
 [0.9494001018303374, 0.48147765150717164, 0.19634119537010658],
 [0.9367761093066895, 0.4903289861634961, 0.19621217170366745],
 [0.9247857607055284, 0.4984135311809655, 0.1960916507741532],
 [0.9133652463841355, 0.5058390026687045, 0.1959786878320478],
 [0.9024586392133133, 0.5126935243797959, 0.195872470122816],
 [0.8920166625769809, 0.5190499999134427, 0.19577229444561794],
 [0.8819956828512875, 0.5249693412027119, 0.19567754913186025],
 [0.8723568794621414, 0.5305028938447651, 0.19558769945962756],
 [0.8630655565519593, 0.5356942869524188, 0.19550227576271062],
 [0.8540905684159935, 0.5405808632704622, 0.1954208636701063],
 [0.8454038369750382, 0.5451947982729264, 0.19534309604298805],
 [0.8369799441810588, 0.5495639855118556, 0.19526864627374518],
 [0.828795785793166, 0.5537127440336859, 0.19519722268536394],
 [0.8208302756915257, 0.5576623887746345, 0.19512856382527483],
 [0.8130640920179332, 0.5614316943215777, 0.19506243449061011],
 [0.8054794580914418, 0.5650372748818442, 0.19499862235491514],
 [0.7980599523546124, 0.5684938978257998, 0.19493693509195814],
 [0.7907903426417726, 0.5718147441360021, 0.19487719791246438],
 [0.7836564408861008, 0.5750116260987126, 0.19481925144542736],
 [0.7766449750434069, 0.5780951703198088, 0.19476294990818424],
 [0.7697434755422866, 0.581074972436332, 0.1947081595195062],
 [0.7629401739997329, 0.5839597285844569, 0.1946547571179253],
 [0.756223912288999, 0.5867573476724397, 0.1946026289540423],
 [0.7495840603285927, 0.5894750477190511, 0.19455166963076145],
 [0.7430104411901503, 0.5921194388999992, 0.19450178116968828],
 [0.7364932623083359, 0.5946965954568577, 0.194452872185375],
 [0.7300230517253895, 0.5972121182352164, 0.19440485715201183],
 [0.7235905984223692, 0.5996711893087466, 0.1943576557494367],
 [0.7171868958830482, 0.6020786198966316, 0.19431119227735008],
 [0.7108030881082806, 0.604438892580396, 0.19426539512819752],
 [0.704430417350955, 0.6067561986626179, 0.19422019631050969],
 [0.6980601728762077, 0.6090344713766105, 0.19417553101562343],
 [0.6916836400694251, 0.6112774155469421, 0.1941313372216396],
 [0.6852920492161709, 0.6134885342109139, 0.19408755532920197],
 [0.6788765232633583, 0.6156711526371499, 0.19404412782436364],
 [0.6724280238388817, 0.6178284401163767, 0.19400099896433368],
 [0.665937294756032, 0.619963429848937, 0.19395811448232542],
 [0.6593948021569331, 0.622079037211774, 0.1939154213080708],
 [0.6527906703526335, 0.6241780766530699, 0.19387286730090741],
 [0.6461146122918401, 0.6262632774342325, 0.19383040099250096],
 [0.6393558534294527, 0.6283372984155824, 0.19378797133651432],
 [0.6325030475620563, 0.6304027420631343, 0.19374552746258544],
 [0.6255441829396258, 0.63246216783871, 0.19370301843211374],
 [0.61846647663684, 0.6345181051237989, 0.1936603929933482]];
phase_colormap = ListedColormap(cm_data, name='phase')