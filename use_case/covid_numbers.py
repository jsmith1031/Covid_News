import requests
from bs4 import BeautifulSoup as bs
#
def covid_numbers(county):


    diction = {'22193': 'Prince William', '23464': 'Virginia Beach City', '22191': 'Prince William', '23462': 'Virginia Beach City', '23322': 'Chesapeake City', '20147': 'Loudoun', '22003': 'Fairfax', '22030': 'Fairfax City', '23452': 'Virginia Beach City', '23454': 'Virginia Beach City', '22407': 'Spotsylvania', '22192': 'Prince William', '23320': 'Chesapeake City', '22554': 'Stafford', '24060': 'Montgomery', '22204': 'Arlington', '23456': 'Virginia Beach City', '23112': 'Chesterfield', '20176': 'Loudoun', '23223': 'Richmond City', '23666': 'Hampton City', '20148': 'Loudoun', '20171': 'Fairfax', '23434': 'Suffolk City', '23455': 'Virginia Beach City', '22304': 'Alexandria City', '23185': 'James City', '20110': 'Manassas City', '24502': 'Lynchburg City', '23234': 'Chesterfield', '22015': 'Fairfax', '23188': 'James City', '23451': 'Virginia Beach City', '20109': 'Manassas City', '23608': 'Newport News City', '23225': 'Richmond City', '20170': 'Fairfax', '20164': 'Loudoun', '22801': 'Harrisonburg City', '20120': 'Fairfax', '23323': 'Chesapeake City', '23669': 'Hampton City', '22903': 'Charlottesville City', '23224': 'Richmond City', '22033': 'Fairfax', '23602': 'Newport News City', '22201': 'Arlington', '24018': 'Roanoke', '23832': 'Chesterfield', '23803': 'Petersburg City', '24153': 'Salem', '23060': 'Henrico', '22309': 'Fairfax', '23111': 'Hanover', '20155': 'Prince William', '23231': 'Henrico', '22079': 'Fairfax', '20111': 'Manassas Park City', '23321': 'Chesapeake City', '23059': 'Hanover', '23831': 'Chesterfield', '24401': 'Staunton City', '23228': 'Henrico', '22701': 'Culpeper', '22306': 'Fairfax', '22901': 'Albemarle', '23229': 'Henrico', '20152': 'Loudoun', '22042': 'Fairfax', '23220': 'Richmond City', '20175': 'Loudoun', '22314': 'Alexandria City', '22031': 'Fairfax City', '22207': 'Arlington', '23235': 'Chesterfield', '22312': 'Fairfax', '22310': 'Fairfax', '22980': 'Waynesboro City', '22630': 'Warren', '23503': 'Norfolk City', '20165': 'Loudoun', '22405': 'Stafford', '24540': 'Danville City', '23233': 'Henrico', '22032': 'Fairfax', '22153': 'Fairfax', '23116': 'Hanover', '24073': 'Montgomery', '23435': 'Suffolk City', '22152': 'Fairfax', '23860': 'Hopewell City', '23513': 'Norfolk City', '22408': 'Spotsylvania', '23505': 'Norfolk City', '24012': 'Roanoke City', '20191': 'Fairfax', '22101': 'Fairfax', '20136': 'Prince William', '22602': 'Frederick', '22315': 'Fairfax', '24112': 'Martinsville City', '20121': 'Fairfax', '23518': 'Norfolk City', '22802': 'Rockingham', '22601': 'Winchester City', '22150': 'Fairfax', '23606': 'Newport News City', '22401': 'Fredericksburg City', '22041': 'Fairfax', '24501': 'Lynchburg City', '24019': 'Botetourt', '23222': 'Richmond City', '24541': 'Danville City', '23703': 'Portsmouth City', '20112': 'Manassas Park City', '22406': 'Stafford', '23238': 'Goochland', '22182': 'Fairfax', '23834': 'Colonial Heights City', '23227': 'Henrico', '22102': 'Fairfax', '24551': 'Bedford', '20169': 'Prince William', '22485': 'King George', '22202': 'Arlington', '22902': 'Charlottesville City', '20105': 'Loudoun', '23113': 'Chesterfield', '23601': 'Newport News City', '22043': 'Fairfax', '23237': 'Chesterfield', '23139': 'Powhatan', '22180': 'Fairfax', '23693': 'York', '22203': 'Arlington', '23236': 'Chesterfield', '23701': 'Portsmouth City', '23324': 'Chesapeake City', '24017': 'Roanoke City', '23504': 'Norfolk City', '20151': 'Fairfax', '23607': 'Newport News City', '24141': 'Radford', '22655': 'Frederick', '23508': 'Norfolk City', '23502': 'Norfolk City', '23061': 'Gloucester', '22206': 'Arlington', '24151': 'Franklin', '20190': 'Fairfax', '24523': 'Bedford City', '23114': 'Chesterfield', '23805': 'Petersburg City', '24503': 'Lynchburg City', '22311': 'Alexandria City', '22205': 'Arlington', '20187': 'Fauquier', '22046': 'Falls Church City', '22305': 'Alexandria City', '22124': 'Fairfax', '23901': 'Prince Edward', '23692': 'York', '24179': 'Roanoke', '23294': 'Henrico', '20132': 'Loudoun', '22151': 'Fairfax', '24333': 'Galax City', '22066': 'Fairfax', '23005': 'Hanover', '22039': 'Fairfax', '23704': 'Portsmouth City', '22302': 'Alexandria City', '22911': 'Albemarle', '23430': 'Isle Of Wight', '24450': 'Lexington City', '24572': 'Amherst', '23838': 'Chesterfield', '24014': 'Roanoke City', '22963': 'Fluvanna', '22026': 'Prince William', '23226': 'Henrico', '24210': 'Washington', '22546': 'Caroline', '24201': 'Bristol', '23325': 'Chesapeake City', '22603': 'Frederick', '22553': 'Spotsylvania', '23847': 'Emporia City', '22181': 'Fairfax', '20124': 'Fairfax', '23221': 'Richmond City', '20186': 'Fauquier', '22508': 'Orange', '23707': 'Portsmouth City', '24015': 'Roanoke City', '22303': 'Fairfax', '24301': 'Pulaski', '23093': 'Louisa', '24354': 'Smyth', '23605': 'Newport News City', '23836': 'Chesterfield', '24382': 'Wythe', '23511': 'Norfolk City', '22044': 'Fairfax', '22308': 'Fairfax', '23509': 'Norfolk City', '23663': 'Hampton City', '24426': 'Covington City', '23851': 'Franklin City', '22301': 'Alexandria City', '24592': 'Halifax', '22209': 'Arlington', '23150': 'Henrico', '23661': 'Hampton City', '20194': 'Fairfax', '24055': 'Henry', '23072': 'Gloucester', '23875': 'Prince George', '20166': 'Loudoun', '23662': 'Poquoson City', '22835': 'Page', '24219': 'Wise', '24121': 'Bedford', '24202': 'Bristol', '23702': 'Portsmouth City', '24084': 'Pulaski', '24477': 'Augusta', '22657': 'Shenandoah', '22968': 'Greene', '23120': 'Chesterfield', '22827': 'Rockingham', '22960': 'Orange', '24211': 'Washington', '23002': 'Amelia', '24588': 'Campbell', '22172': 'Prince William', '22307': 'Fairfax', '24521': 'Amherst', '22942': 'Orange', '24504': 'Lynchburg City', '24343': 'Carroll', '23664': 'Hampton City', '24293': 'Wise', '22060': 'Fairfax', '22664': 'Shenandoah', '23075': 'Henrico', '23117': 'Louisa', '20181': 'Prince William', '22815': 'Rockingham', '23314': 'Isle Of Wight', '24522': 'Appomattox', '22712': 'Fauquier', '24266': 'Russell', '22611': 'Clarke', '22812': 'Rockingham', '23510': 'Norfolk City', '22443': 'Westmoreland', '24531': 'Pittsylvania', '24016': 'Roanoke City', '24416': 'Buena Vista City', '23970': 'Mecklenburg', '23024': 'Louisa', '24013': 'Roanoke City', '24148': 'Henry', '24171': 'Patrick', '24251': 'Scott', '23936': 'Buckingham', '24175': 'Botetourt', '24230': 'Wise', '24605': 'Tazewell', '20141': 'Loudoun', '24590': 'Albemarle', '24091': 'Floyd', '22932': 'Albemarle', '20180': 'Loudoun', '23168': 'James City', '24557': 'Pittsylvania', '23523': 'Norfolk City', '22134': 'Prince William', '24078': 'Henry', '24550': 'Campbell', '24319': 'Smyth', '22572': 'Richmond', '24614': 'Buchanan', '24630': 'Tazewell', '20115': 'Fauquier', '24609': 'Tazewell', '23141': 'New Kent', '23868': 'Brunswick', '24277': 'Lee', '23192': 'Hanover', '23604': 'Newport News City', '23230': 'Henrico', '24370': 'Smyth', '23507': 'Norfolk City', '23009': 'King William', '23824': 'Nottoway', '23842': 'Prince George', '24228': 'Dickenson', '22560': 'Essex', '23140': 'New Kent', '22939': 'Augusta', '24054': 'Henry', '23665': 'Hampton City', '24101': 'Bedford', '22824': 'Shenandoah', '24441': 'Rockingham', '24065': 'Franklin', '24273': 'Norton City', '22851': 'Page', '24340': 'Washington', '24422': 'Alleghany', '22973': 'Greene', '24244': 'Scott', '24263': 'Lee', '24224': 'Russell', '24586': 'Pittsylvania', '24558': 'Halifax', '24360': 'Wythe', '24361': 'Washington', '22727': 'Madison', '23801': 'Prince George', '23487': 'Isle Of Wight', '23089': 'New Kent', '24651': 'Tazewell', '22923': 'Orange', '22520': 'Westmoreland', '23924': 'Mecklenburg', '23974': 'Lunenburg', '24538': 'Campbell', '23103': 'Goochland', '24641': 'Tazewell', '24088': 'Franklin', '22821': 'Rockingham', '22842': 'Shenandoah', '22427': 'Caroline', '24260': 'Russell', '22849': 'Page', '24066': 'Botetourt', '24563': 'Pittsylvania', '24482': 'Augusta', '24368': 'Wythe', '24279': 'Wise', '23181': 'King William', '24134': 'Giles', '22974': 'Fluvanna', '20106': 'Rappahannock', '22580': 'Caroline', '22473': 'Northumberland', '24064': 'Botetourt', '24090': 'Botetourt', '22642': 'Warren', '23930': 'Nottoway', '22936': 'Albemarle', '22904': 'Charlottesville City', '22844': 'Shenandoah', '24124': 'Giles', '23030': 'Charles City', '24348': 'Grayson', '23040': 'Cumberland', '24517': 'Campbell', '24577': 'Halifax', '23063': 'Goochland', '22840': 'Rockingham', '20158': 'Loudoun', '24184': 'Franklin', '23922': 'Nottoway', '23517': 'Norfolk City', '23124': 'New Kent', '23219': 'Richmond City', '23421': 'Accomack', '23837': 'Southampton', '23890': 'Sussex', '23690': 'York', '23310': 'Northampton', '24095': 'Bedford', '23437': 'Suffolk City', '22645': 'Frederick', '23457': 'Virginia Beach City', '23927': 'Mecklenburg', '24421': 'Augusta', '24574': 'Amherst', '22853': 'Rockingham', '22947': 'Albemarle', '24554': 'Campbell', '23947': 'Charlotte', '23603': 'Newport News City', '24317': 'Carroll', '22920': 'Nelson', '23950': 'Mecklenburg', '24127': 'Craig', '23015': 'Hanover', '20119': 'Fauquier', '24430': 'Augusta', '24381': 'Carroll', '24549': 'Pittsylvania', '24087': 'Roanoke', '23420': 'Accomack', '22213': 'Arlington', '23696': 'York', '24637': 'Tazewell', '23086': 'King William', '24315': 'Bland', '22567': 'Orange', '23350': 'Northampton', '22656': 'Frederick', '22734': 'Fauquier', '24256': 'Dickenson', '22625': 'Frederick', '24104': 'Bedford', '23417': 'Accomack', '24639': 'Buchanan', '24149': 'Montgomery', '22737': 'Culpeper', '23958': 'Appomattox', '23102': 'Goochland', '24486': 'Augusta', '23841': 'Dinwiddie', '23146': 'Hanover', '22534': 'Spotsylvania', '24556': 'Bedford', '22503': 'Lancaster', '20135': 'Loudoun', '22482': 'Lancaster', '24589': 'Halifax', '22807': 'Harrisonburg City', '24136': 'Giles', '24528': 'Campbell', '23149': 'Middlesex', '23944': 'Lunenburg', '24236': 'Washington', '23923': 'Charlotte', '24330': 'Grayson', '23920': 'Brunswick', '24440': 'Augusta', '24620': 'Buchanan', '24083': 'Botetourt', '24656': 'Buchanan', '23336': 'Accomack', '24174': 'Bedford', '24527': 'Pittsylvania', '23069': 'Hanover', '22728': 'Fauquier', '22624': 'Frederick', '24445': 'Bath', '23917': 'Mecklenburg', '22735': 'Culpeper', '22841': 'Rockingham', '24142': 'Radford', '23840': 'Dinwiddie', '24216': 'Wise', '24649': 'Russell', '24380': 'Floyd', '22620': 'Clarke', '24053': 'Patrick', '23083': 'Amelia', '24431': 'Augusta', '23160': 'Goochland', '23872': 'Dinwiddie', '23885': 'Dinwiddie', '24137': 'Franklin', '22578': 'Lancaster', '22576': 'Lancaster', '22843': 'Augusta', '24281': 'Lee', '22435': 'Northumberland', '20197': 'Loudoun', '24248': 'Lee', '23829': 'Southampton', '24092': 'Franklin', '22637': 'Frederick', '24089': 'Henry', '23919': 'Mecklenburg', '23888': 'Sussex', '24162': 'Montgomery', '22644': 'Shenandoah', '24067': 'Franklin', '24467': 'Augusta', '24631': 'Buchanan', '22937': 'Albemarle', '24271': 'Scott', '24571': 'Campbell', '20117': 'Loudoun', '22846': 'Rockingham', '23966': 'Prince Edward', '24225': 'Russell', '24520': 'Halifax', '24593': 'Appomattox', '24133': 'Patrick', '23062': 'Gloucester', '24555': 'Rockbridge', '22539': 'Northumberland', '23173': 'Richmond City', '23833': 'Dinwiddie', '22514': 'Caroline', '23898': 'Isle Of Wight', '22922': 'Nelson', '24085': 'Botetourt', '23882': 'Sussex', '23308': 'Accomack', '24283': 'Wise', '23891': 'Sussex', '22724': 'Culpeper', '23109': 'Mathews', '23883': 'Surry', '24529': 'Mecklenburg', '22967': 'Nelson', '23043': 'Middlesex', '24435': 'Rockbridge', '23460': 'Virginia Beach City', '23881': 'Surry', '23821': 'Brunswick', '22027': 'Fairfax', '22958': 'Nelson', '23866': 'Southampton', '24290': 'Scott', '24128': 'Giles', '24243': 'Lee', '22660': 'Shenandoah', '23867': 'Sussex', '23123': 'Buckingham', '20198': 'Fauquier', '23084': 'Fluvanna', '22742': 'Fauquier', '24375': 'Smyth', '23047': 'Hanover', '22830': 'Rockingham', '22969': 'Nelson', '24324': 'Pulaski', '24070': 'Roanoke', '24079': 'Floyd', '23156': 'King And Queen', '23148': 'King And Queen', '23438': 'Suffolk City', '23937': 'Charlotte', '22952': 'Augusta', '24471': 'Rockingham', '22542': 'Orange', '22971': 'Nelson', '24328': 'Carroll', '22454': 'Essex', '22469': 'Westmoreland', '22610': 'Warren', '24472': 'Rockbridge', '22713': 'Culpeper', '23301': 'Accomack', '24312': 'Wythe', '24598': 'Halifax', '23954': 'Prince Edward', '24069': 'Pittsylvania', '23806': 'Petersburg City', '24347': 'Pulaski', '24138': 'Montgomery', '23415': 'Accomack', '24122': 'Bedford', '24594': 'Pittsylvania', '24258': 'Scott', '23175': 'Middlesex', '23830': 'Dinwiddie', '24102': 'Franklin', '22652': 'Shenandoah', '23960': 'Prince Edward', '24479': 'Augusta', '20137': 'Fauquier', '23071': 'Middlesex', '23035': 'Mathews', '23038': 'Goochland', '22738': 'Madison', '23432': 'Suffolk City', '23827': 'Southampton', '24553': 'Nelson', '24120': 'Patrick', '24311': 'Smyth', '23065': 'Goochland', '23459': 'Virginia Beach City', '24635': 'Tazewell', '24147': 'Giles', '22709': 'Madison', '22940': 'Albemarle', '24314': 'Bland', '24566': 'Pittsylvania', '22959': 'Albemarle', '22938': 'Nelson', '23153': 'Goochland', '22747': 'Rappahannock', '24076': 'Patrick', '22211': 'Arlington', '23011': 'New Kent', '22460': 'Richmond', '23410': 'Accomack', '22729': 'Culpeper', '24250': 'Scott', '23921': 'Buckingham', '24363': 'Grayson', '23964': 'Charlotte', '24526': 'Bedford', '23442': 'Accomack', '24165': 'Henry', '24176': 'Franklin', '24579': 'Rockbridge', '24465': 'Highland', '23942': 'Prince Edward', '22715': 'Madison', '24439': 'Rockbridge', '23915': 'Mecklenburg', '23433': 'Suffolk City', '23315': 'Isle Of Wight', '23850': 'Dinwiddie', '24534': 'Halifax', '22831': 'Rockingham', '23959': 'Charlotte', '23551': 'Norfolk City', '23356': 'Accomack', '24460': 'Bath', '24350': 'Wythe', '24226': 'Dickenson', '24597': 'Halifax', '23967': 'Charlotte', '22714': 'Culpeper', '23027': 'Cumberland', '22663': 'Clarke', '22850': 'Rockingham', '20144': 'Fauquier', '22832': 'Rockingham', '24599': 'Nelson', '23169': 'Middlesex', '22949': 'Nelson', '23039': 'Goochland', '22834': 'Rockingham', '24220': 'Dickenson', '22720': 'Fauquier', '24326': 'Grayson', '24072': 'Floyd', '24325': 'Carroll', '23106': 'King William', '23436': 'Suffolk City', '24378': 'Grayson', '23878': 'Southampton', '22623': 'Rappahannock', '22935': 'Greene', '23418': 'Accomack', '22125': 'Prince William', '24569': 'Campbell', '23839': 'Surry', '24530': 'Pittsylvania', '24578': 'Rockbridge', '23874': 'Southampton', '23405': 'Northampton', '22733': 'Culpeper', '24313': 'Wythe', '23022': 'Fluvanna', '23856': 'Brunswick', '24323': 'Wythe', '24473': 'Rockbridge', '22437': 'Essex', '22654': 'Frederick', '22740': 'Rappahannock', '23076': 'Mathews', '22511': 'Northumberland', '24282': 'Lee', '24237': 'Russell', '22847': 'Shenandoah', '22488': 'Westmoreland', '24059': 'Roanoke', '23846': 'Surry', '24280': 'Russell', '24352': 'Carroll', '24622': 'Tazewell', '23962': 'Charlotte', '23407': 'Accomack', '20143': 'Prince William', '24150': 'Giles', '24565': 'Pittsylvania', '22736': 'Culpeper', '23894': 'Dinwiddie', '24270': 'Washington', '24374': 'Wythe', '24077': 'Botetourt', '23129': 'Goochland', '24603': 'Buchanan', '23306': 'Accomack', '23055': 'Fluvanna', '24245': 'Scott', '23004': 'Buckingham', '23889': 'Brunswick', '23357': 'Accomack', '22726': 'Culpeper', '22436': 'Essex', '23347': 'Northampton', '24459': 'Augusta', '24272': 'Dickenson', '24265': 'Lee', '23128': 'Mathews', '24437': 'Augusta', '23307': 'Northampton', '22627': 'Rappahannock', '23857': 'Brunswick', '23709': 'Portsmouth City', '23050': 'Gloucester', '23023': 'King And Queen', '24474': 'Alleghany', '24602': 'Tazewell', '23359': 'Accomack', '23177': 'King And Queen', '24082': 'Patrick', '22480': 'Lancaster', '22448': 'King George', '24646': 'Buchanan', '23413': 'Northampton', '24595': 'Amherst', '23180': 'Middlesex', '24020': 'Roanoke', '23138': 'Mathews', '22811': 'Rockingham', '22810': 'Shenandoah', '23844': 'Southampton', '23968': 'Mecklenburg', '24318': 'Bland', '24221': 'Lee', '23303': 'Accomack', '22976': 'Nelson', '24483': 'Rockbridge', '23092': 'Middlesex', '24613': 'Tazewell', '23395': 'Accomack', '23085': 'King And Queen', '22535': 'Caroline', '24484': 'Bath', '24366': 'Bland', '22639': 'Fauquier', '22943': 'Albemarle', '24580': 'Mecklenburg', '22718': 'Culpeper', '24562': 'Albemarle', '23934': 'Charlotte', '20129': 'Loudoun', '23316': 'Northampton', '23845': 'Brunswick', '24011': 'Roanoke City', '23897': 'Sussex', '23879': 'Greensville', '22548': 'Richmond', '23708': 'Portsmouth City', '22716': 'Rappahannock', '23440': 'Accomack', '24161': 'Pittsylvania', '22650': 'Page', '23126': 'King And Queen', '20184': 'Fauquier', '24246': 'Wise', '23651': 'Hampton City', '24105': 'Floyd', '24634': 'Buchanan', '22640': 'Rappahannock', '24185': 'Patrick', '23461': 'Virginia Beach City', '23909': 'Prince Edward', '24351': 'Carroll', '23337': 'Accomack', '23056': 'Mathews', '22433': 'Orange', '23423': 'Accomack', '23843': 'Brunswick', '23032': 'Middlesex', '23079': 'Middlesex', '23125': 'Mathews', '24458': 'Highland', '24292': 'Grayson', '24269': 'Dickenson', '23110': 'King And Queen', '24168': 'Henry', '22504': 'Essex', '24657': 'Buchanan', '23480': 'Accomack', '23176': 'Middlesex', '23488': 'Accomack', '24139': 'Pittsylvania', '22641': 'Shenandoah', '22438': 'Essex', '23828': 'Southampton', '24485': 'Augusta', '23899': 'Surry', '24377': 'Tazewell', '23070': 'Middlesex', '24487': 'Bath', '23021': 'Mathews', '23119': 'Mathews', '23887': 'Brunswick', '22964': 'Nelson', '22643': 'Fauquier', '22820': 'Rockingham', '23893': 'Brunswick', '24432': 'Augusta', '24536': 'Bedford', '24132': 'Pulaski', '24217': 'Dickenson', '22931': 'Albemarle', '24413': 'Highland', '22972': 'Orange', '23876': 'Brunswick', '22743': 'Madison', '24448': 'Alleghany', '22719': 'Madison', '24607': 'Dickenson', '23064': 'Mathews', '23187': 'Williamsburg City', '24628': 'Buchanan', '20139': 'Fauquier', '23091': 'King And Queen', '22722': 'Madison', '24058': 'Pulaski', '22432': 'Northumberland', '24239': 'Buchanan', '22476': 'Essex', '23952': 'Lunenburg', '23427': 'Accomack', '20130': 'Fauquier', '23938': 'Lunenburg', '22749': 'Rappahannock', '24476': 'Augusta', '22730': 'Madison', '23130': 'Mathews', '23389': 'Accomack', '22732': 'Madison', '24606': 'Tazewell', '24457': 'Alleghany', '24167': 'Giles', '23068': 'Mathews', '24604': 'Tazewell', '23313': 'Northampton', '23025': 'Mathews', '23414': 'Accomack', '24464': 'Nelson', '22530': 'Northumberland', '23416': 'Accomack', '22741': 'Culpeper', '24612': 'Tazewell', '22948': 'Madison', '23302': 'Accomack', '23354': 'Northampton', '23409': 'Accomack', '22529': 'Westmoreland', '23691': 'York', '23401': 'Accomack', '23422': 'Accomack', '22946': 'Albemarle', '23045': 'Mathews', '23441': 'Accomack', '24442': 'Highland', '22538': 'Caroline', '22723': 'Madison', '24086': 'Giles', '23161': 'King And Queen', '22509': 'Essex', '24093': 'Giles', '23066': 'Mathews', '24322': 'Wythe', '23426': 'Accomack', '23358': 'Accomack', '23108': 'King And Queen', '23963': 'Charlotte', '22646': 'Clarke', '24539': 'Halifax', '24433': 'Highland', '22579': 'Northumberland', '23408': 'Northampton', '23943': 'Prince Edward', '24411': 'Augusta', '23115': 'Essex', '22731': 'Madison', '23884': 'Sussex', '23304': 'Isle Of Wight', '23976': 'Charlotte', '23398': 'Northampton', '23163': 'Mathews', '24412': 'Bath', '24581': 'Nelson', '22711': 'Madison', '23486': 'Northampton', '22989': 'Madison', '24130': 'Botetourt', '24131': 'Craig', '22845': 'Shenandoah', '20118': 'Loudoun', '23250': 'Henrico', '24415': 'Rockbridge', '22214': 'Arlington', '24601': 'Tazewell', '24316': 'Smyth', '22035': 'Fairfax', '22185': 'Fairfax'}

    #GET COUNTY NAME AS INPUT
    for k, v in diction.items():
        zip = str(county)
        if k == zip:
            cty = v
            countyy = v.lower()
            dic={}
            #PREPARE THE URL TO ACCESS THE NEWS SITE
            u1 = "https://www.nytimes.com/interactive/2021/us/"
            u2 = "-virginia-covid-cases.html"
            url = u1+countyy+u2
            u11= "https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/state/virginia/county/"
            url1 = u11+countyy+"-county"

            #ACCESS THE WEBSITE
            r = requests.get(url)
            p = requests.get(url1)

            #PARSE THE PAGE INTO HTML TO PROCESS THE DATA
            html = r.content
            bb= p.content
            soup = bs(html,'html.parser')
            sp = bs(bb,'html.parser')

            print(f"Cases for {countyy} county: ")

            # RETRIEVING DAILY CASES FROM USAFACTS WEBSITE
            h11 = sp.find('tbody',class_='MuiTableBody-root')

            dc = h11.find_all('td',class_='MuiTableCell-root')

            if(int(dc[1].string)<0):
                print("Today's Cases: 0")
                
            else:
                print("Today's Cases: ",dc[1].string)
                
            if(int(dc[3].string)<0):
                print("Today's Deaths: 0")
               
            else:
                print("Today's Deaths: ",dc[3].string)
                



            # RETRIEVING 7 DAYS AVERAGE CASES FROM NEWYORK TIMES WEBSITE
            h = soup.find('tbody', class_='parent super')
            k = soup.find('table',class_='g-table top-summary')
            cases = k.find('td',class_='num cases svelte-17z9x2b')
            print("7 DAY AVERAGE")
            
            print("Cases : ",cases.string)
           
            hospitalized = k.find('td',class_='num hospitalized svelte-17z9x2b')
            print("Hospitalized: ",hospitalized.string)
            
            death = k.find('td',class_='num deaths svelte-17z9x2b')
            print("Death: ",death.string)
            
            

            
zc = input("Please enter valid 5 digit zipcode: ")
covid_numbers(zc)




