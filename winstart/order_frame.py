import os.path
from datetime import datetime

from PyQt5 import QtWidgets, QtCore

# from dbase.databasecreate import CreateDB
# from dbase.dbapi import APIAxiomDB
# from doc_parser import CreateFile
# from frame.CSS_template import CSS
# from log_setting import logger
from setting import logger



class Order:
    def __init__(self):
        self.frame = QtWidgets.QFrame()
        self.txt_edit_lineEdit_client_owner_name = QtWidgets.QLineEdit(self.frame)
        self.txt_label_order_number = QtWidgets.QLabel(self.frame)
        self.txt_label_brand = QtWidgets.QLabel(self.frame)
        self.txt_label_car_number = QtWidgets.QLabel(self.frame)
        self.txt_label_order_number_prefix = QtWidgets.QLabel(self.frame)
        self.txt_label_client_name = QtWidgets.QLabel(self.frame)
        self.txt_label_model = QtWidgets.QLabel(self.frame)
        self.txt_edit_lineEdit_client_job_title = QtWidgets.QLineEdit(self.frame)
        self.txt_label_vin_code = QtWidgets.QLabel(self.frame)
        self.txt_label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.btn_pushButton_refresh = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_new_client = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_part_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_order_close = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_car_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_new_car = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_print_order = QtWidgets.QPushButton(self.frame)
        self.checkBox_1_repair_request = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2_application_order = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3_act_of_acceptance = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4_internal_consumption = QtWidgets.QCheckBox(self.frame)
        self.frame_data = QtWidgets.QFrame(self.frame)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_data)
        self.label_client_job_title = QtWidgets.QLabel(self.frame)
        self.label_client_name = QtWidgets.QLabel(self.frame)
        self.label_client_owner_name = QtWidgets.QLabel(self.frame)
        self.label_order_number = QtWidgets.QLabel(self.frame)
        self.label_order_number_sep = QtWidgets.QLabel(self.frame)
        self.label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.driver_item = []

        self.dict_label = {
            'brand': self.txt_label_brand,
            'number_car': self.txt_label_car_number,
            'model': self.txt_label_model,
            'vin_code': self.txt_label_vin_code,
            'order_number': self.txt_label_order_number,
            'prefix': self.txt_label_order_number_prefix,
            'driver_name': self.txt_edit_lineEdit_client_owner_name,
            'job_title': self.txt_edit_lineEdit_client_job_title,
            'client_name': self.txt_label_client_name,
            'client_unp': self.txt_label_client_identification_number,
        }

        self.current_id = None

    @logger.logger.catch
    def set_frame(self, frame):
        self.frame = QtWidgets.QFrame(frame)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 593))
        self.frame.setMinimumSize(QtCore.QSize(571, 593))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.set_body()
        return self.frame

    def set_body(self):
        self.txt_edit_lineEdit_client_owner_name = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_owner_name.setGeometry(QtCore.QRect(128, 190, 425, 31))
        self.txt_edit_lineEdit_client_owner_name.setAutoFillBackground(True)
        self.txt_edit_lineEdit_client_owner_name.setClearButtonEnabled(True)
        self.txt_edit_lineEdit_client_owner_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_owner_name.setPlaceholderText("ФИО заказчика")
        self.txt_edit_lineEdit_client_owner_name.setObjectName("txt_edit_lineEdit_client_owner_name")
        # self.txt_edit_lineEdit_client_owner_name.setTextMargins(CSS.set_margins())

        self.txt_label_order_number = QtWidgets.QLabel(self.frame)
        self.txt_label_order_number.setGeometry(QtCore.QRect(235, 48, 91, 30))
        # self.txt_label_order_number.setFont(CSS.set_font(14, True, 75))
        self.txt_label_order_number.setAutoFillBackground(False)
        self.txt_label_order_number.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_order_number.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.txt_label_order_number.setObjectName("txt_label_order_number")
        self.txt_label_order_number.setIndent(10)

        self.txt_label_brand = QtWidgets.QLabel(self.frame)
        self.txt_label_brand.setGeometry(QtCore.QRect(128, 350, 181, 30))
        # self.txt_label_brand.setFont(CSS.set_font(12, False, 50))
        self.txt_label_brand.setAutoFillBackground(False)
        self.txt_label_brand.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_brand.setObjectName("txt_label_brand")
        self.txt_label_brand.setIndent(10)

        self.txt_label_car_number = QtWidgets.QLabel(self.frame)
        self.txt_label_car_number.setGeometry(QtCore.QRect(318, 350, 141, 30))
        # self.txt_label_car_number.setFont(CSS.set_font(12, False, 50))
        self.txt_label_car_number.setAutoFillBackground(False)
        self.txt_label_car_number.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_car_number.setObjectName("txt_label_car_number")
        self.txt_label_car_number.setIndent(10)

        self.txt_label_order_number_prefix = QtWidgets.QLabel(self.frame)
        self.txt_label_order_number_prefix.setGeometry(QtCore.QRect(358, 48, 31, 30))
        # self.txt_label_order_number_prefix.setFont(CSS.set_font(14, True, 75))
        self.txt_label_order_number_prefix.setAutoFillBackground(False)
        self.txt_label_order_number_prefix.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_order_number_prefix.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_label_order_number_prefix.setObjectName("txt_label_order_number_prefix")

        self.txt_label_client_name = QtWidgets.QLabel(self.frame)
        self.txt_label_client_name.setGeometry(QtCore.QRect(128, 110, 331, 30))
        # self.txt_label_client_name.setFont(CSS.set_font(12, False, 50))
        self.txt_label_client_name.setAutoFillBackground(True)
        self.txt_label_client_name.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_client_name.setObjectName("txt_label_client_name")
        self.txt_label_client_name.setIndent(10)

        self.txt_label_model = QtWidgets.QLabel(self.frame)
        self.txt_label_model.setGeometry(QtCore.QRect(128, 390, 331, 30))
        # self.txt_label_model.setFont(CSS.set_font(12, False, 50))
        self.txt_label_model.setAutoFillBackground(False)
        self.txt_label_model.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_model.setObjectName("txt_label_model")
        self.txt_label_model.setIndent(10)

        # self.combo_box = QtWidgets.QComboBox(self.frame)
        # self.combo_box.setGeometry(QtCore.QRect(128, 190, 425, 31))
        # self.combo_box.setFont(CSS.set_font(12, False, 50))
        # self.combo_box.setAutoFillBackground(False)
        # self.combo_box.setStyleSheet("background-color: rgb(221, 221, 221);")
        # self.combo_box.setObjectName("combo_box")

        self.txt_edit_lineEdit_client_job_title = QtWidgets.QLineEdit(self.frame)
        self.txt_edit_lineEdit_client_job_title.setGeometry(QtCore.QRect(128, 150, 333, 31))
        self.txt_edit_lineEdit_client_job_title.setAutoFillBackground(True)
        self.txt_edit_lineEdit_client_job_title.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_edit_lineEdit_client_job_title.setObjectName("txt_edit_lineEdit_client_job_title")
        self.txt_edit_lineEdit_client_job_title.setPlaceholderText("Должность заказчика")
        self.txt_edit_lineEdit_client_job_title.setClearButtonEnabled(True)
        # self.txt_edit_lineEdit_client_job_title.setTextMargins(CSS.set_margins())

        self.txt_label_vin_code = QtWidgets.QLabel(self.frame)
        self.txt_label_vin_code.setGeometry(QtCore.QRect(128, 430, 425, 30))
        # self.txt_label_vin_code.setFont(CSS.set_font(12, False, 50))
        self.txt_label_vin_code.setAutoFillBackground(False)
        self.txt_label_vin_code.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_vin_code.setObjectName("txt_label_vin_code")
        self.txt_label_vin_code.setIndent(10)

        self.txt_label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.txt_label_client_identification_number.setGeometry(QtCore.QRect(128, 230, 425, 30))
        # self.txt_label_client_identification_number.setFont(CSS.set_font(12, False, 50))
        self.txt_label_client_identification_number.setAutoFillBackground(True)
        self.txt_label_client_identification_number.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.txt_label_client_identification_number.setObjectName("txt_label_client_identification_number")
        self.txt_label_client_identification_number.setIndent(10)

        self.set_btn()
        self.set_check_box()
        self.set_datetime()
        self.set_label()
        # self.add_action()
        # self.retranslateUi()

    # @classmethod
    # @logger.catch
    # def clear_txt(cls, txt):
    #     txt.clear()
    #
    # @logger.catch
    # def add_action(self):
    #     self.btn_pushButton_car_part_choice.clicked.connect(lambda: self.part_choice())
    #     self.btn_pushButton_car_car_choice.clicked.connect(lambda: self.car_choice())
    #     self.btn_pushButton_refresh.clicked.connect(lambda: self.refresh())
    #     self.btn_pushButton_print_order.clicked.connect(lambda: self.print())
    #
    # @logger.catch
    # def print(self):
    #     new = CreateDB()
    #     query = APIAxiomDB()
    #     client_item = query.get_client_from_unp(int(self.txt_label_client_identification_number.text()))
    #
    #     dict_order = {
    #         'brand': self.txt_label_brand.text(),
    #         'car_number': self.txt_label_car_number.text(),
    #         'order_number': self.txt_label_order_number.text(),
    #         'company_id': client_item.id,
    #         'company_name': client_item.full_name,
    #         'client_unp': self.txt_label_client_identification_number.text(),
    #         'prefix': self.txt_label_order_number_prefix.text(),
    #         'data': datetime.now().date(),
    #         'driver_name': self.txt_edit_lineEdit_client_owner_name.text(),
    #         'driver_job': self.txt_edit_lineEdit_client_job_title.text(),
    #         'chk_state': [
    #             self.checkBox_1_repair_request.checkState(),
    #             self.checkBox_2_application_order.checkState(),
    #             self.checkBox_3_act_of_acceptance.checkState(),
    #             self.checkBox_4_internal_consumption.checkState()
    #         ]
    #     }
    #
    #     if not self.current_id and dict_order['brand'] == 'Запчасти':
    #         new.car_create(
    #             name=dict_order['brand'],
    #             model=dict_order['brand'],
    #             number=str(dict_order['car_number']),
    #             vin_code=dict_order['brand'],
    #             company_id=dict_order['company_id']
    #
    #         )
    #     temp_dict = {'car_id': query.get_car_from_id(dict_order['car_number'])}
    #     dict_order.update(temp_dict)
    #
    #     if not dict_order['driver_name'] in query.get_list_driver():
    #         new.driver_create(
    #             name=dict_order['driver_name'],
    #             job=dict_order['driver_job'],
    #             company_id=client_item.id
    #         )
    #
    #     driver_item = query.get_driver(dict_order['driver_name'])
    #     if not self.current_id:
    #
    #         new.order_create(
    #             car_id=dict_order['car_id'],
    #             company_id=dict_order['company_id'],
    #             prefix=dict_order['prefix'],
    #             data=dict_order['data'],
    #             first_open=True,
    #             data_close=None,
    #             path_file='',
    #             driver_id=driver_item.id
    #         )
    #
    #         self.checkBox_1_repair_request.setChecked(True)
    #         self.checkBox_2_application_order.setChecked(True)
    #         self.checkBox_3_act_of_acceptance.setChecked(True)
    #         self.checkBox_4_internal_consumption.setChecked(True)
    #
    #         self.current_id = None
    #     else:
    #         new.update_prefix(self.current_id)
    #         order_item = query.get_order_from_id(int(self.txt_label_order_number.text()))
    #         dict_order['prefix'] = order_item.prefix
    #
    #     context_dict = {
    #         'order_id': dict_order['order_number'],
    #         'order_number': '{}'.format(dict_order['order_number']),
    #         'prefix': dict_order['prefix'],
    #         'name': dict_order['company_name'],
    #         'address': client_item.address,
    #         'phone': client_item.telefone,
    #         'mphone': client_item.mobile,
    #         'driver': '{} {}'.format(dict_order['driver_job'], dict_order['driver_name']),
    #         'brand': dict_order['brand'],
    #         'car_number': dict_order['car_number'],
    #         'path_file_dir': os.path.join(
    #             client_item.name,
    #             str(dict_order['data'].year),
    #             str(dict_order['order_number'])
    #         ),
    #         'file_name': '{act}-'.format(
    #             act=dict_order['order_number']
    #             # day=dict_order['data'].day,
    #             # month=dict_order['data'].month
    #         ),
    #         'crdata': '{day}.{month}.{year}'.format(
    #             day=dict_order['data'].day,
    #             month=dict_order['data'].month,
    #             year=dict_order['data'].year
    #         ),
    #         'curdata': '{day}.{month}.{year}'.format(
    #             day=datetime.now().day,
    #             month=datetime.now().month,
    #             year=datetime.now().year
    #         ),
    #         'chk_state': dict_order['chk_state']
    #     }
    #
    #     CreateFile(context_dict)
    #
    # @logger.catch
    # def refresh(self):
    #     query = APIAxiomDB()
    #     self.txt_label_order_number.setText(str(query.count_act() + 1))
    #     self.txt_label_order_number_prefix.setText('A')
    #
    #     self.checkBox_1_repair_request.setChecked(True)
    #     self.checkBox_2_application_order.setChecked(True)
    #     self.checkBox_3_act_of_acceptance.setChecked(True)
    #     self.checkBox_4_internal_consumption.setChecked(True)
    #
    #     self.txt_label_client_name.setText('название компании')
    #     self.txt_label_client_identification_number.setText(str("УНП клиента"))
    #     self.txt_label_brand.setText("Модель")
    #     self.txt_label_car_number.setText("Номер")
    #     self.txt_label_model.setText("Модель")
    #     self.txt_label_vin_code.setText("УЗМ код")
    #     self.txt_edit_lineEdit_client_owner_name.setText("")
    #     self.txt_edit_lineEdit_client_job_title.setText("")
    #
    #     self.current_id = None
    #
    # @logger.catch
    # def part_choice(self):
    #     """Действие, при нажатии кнопки 'Запчасти'."""
    #
    #     query = APIAxiomDB()
    #     if not self.current_id:
    #         self.txt_label_brand.setText('Запчасти')
    #         self.txt_label_model.setText('Запчасти')
    #         self.txt_label_vin_code.setText('Запчасти')
    #         self.txt_label_car_number.setText(str(query.count_act() + 1))
    #
    #     self.btn_pushButton_car_part_choice.setDown(True)
    #     self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(199, 170, 199);")
    #     self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
    #
    # @logger.catch
    # def car_choice(self):
    #     """Действие, при нажатии кнопки 'Машина'."""
    #
    #     query = APIAxiomDB()
    #     try:
    #         if self.current_id:
    #             car_item = query.get_car_from_order(self.current_id)
    #             self.txt_label_brand.setText(car_item.name)
    #             self.txt_label_car_number.setText(car_item.number)
    #             self.txt_label_model.setText(car_item.model)
    #             self.txt_label_vin_code.setText(car_item.vin_code)
    #         else:
    #             self.txt_label_brand.setText('Машина')
    #             self.txt_label_car_number.setText('Номер')
    #             self.txt_label_model.setText('Модель')
    #             self.txt_label_vin_code.setText('VIN код')
    #
    #         self.btn_pushButton_car_part_choice.setDown(True)
    #         self.btn_pushButton_car_part_choice.setStyleSheet("background-color: rgb(85, 170, 0);")
    #         self.btn_pushButton_car_car_choice.setStyleSheet("background-color: rgb(199, 170, 199);")
    #     except Exception as err:
    #         print(err)
    #
    # @logger.catch
    # def get_fields_car(self):
    #     pass

    @logger.logger.catch
    def set_btn(self):
        self.btn_pushButton_refresh = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_refresh.setGeometry(QtCore.QRect(443, 480, 111, 33))
        # self.btn_pushButton_refresh.setFont(CSS.set_font(12, False, 50))
        self.btn_pushButton_refresh.setAutoFillBackground(False)
        # self.btn_pushButton_refresh.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_refresh.setFont(CSS.set_font())
        self.btn_pushButton_refresh.setObjectName("btn_pushButton_order_close")

        self.btn_pushButton_new_client = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_new_client.setGeometry(QtCore.QRect(468, 110, 85, 71))
        self.btn_pushButton_new_client.setAutoFillBackground(False)
        # self.btn_pushButton_new_client.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_new_client.setFont(CSS.set_font())
        self.btn_pushButton_new_client.setObjectName("btn_pushButton_new_client")

        self.btn_pushButton_car_part_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_part_choice.setGeometry(QtCore.QRect(225, 310, 85, 33))
        self.btn_pushButton_car_part_choice.setAutoFillBackground(False)
        # self.btn_pushButton_car_part_choice.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_car_part_choice.setFont(CSS.set_font())
        self.btn_pushButton_car_part_choice.setObjectName("btn_pushButton_car_part_choice")

        self.btn_pushButton_order_close = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_order_close.setGeometry(QtCore.QRect(443, 50, 111, 33))
        # self.btn_pushButton_order_close.setFont(CSS.set_font(12, False, 50))
        self.btn_pushButton_order_close.setAutoFillBackground(False)
        self.btn_pushButton_order_close.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_pushButton_order_close.setObjectName("btn_pushButton_order_close")

        self.btn_pushButton_car_car_choice = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_car_car_choice.setGeometry(QtCore.QRect(128, 310, 85, 33))
        self.btn_pushButton_car_car_choice.setAutoFillBackground(False)
        # self.btn_pushButton_car_car_choice.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_car_car_choice.setFont(CSS.set_font())
        self.btn_pushButton_car_car_choice.setObjectName("btn_pushButton_car_car_choice")

        self.btn_pushButton_new_car = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_new_car.setGeometry(QtCore.QRect(468, 350, 85, 71))
        self.btn_pushButton_new_car.setAutoFillBackground(False)
        # self.btn_pushButton_new_car.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_new_car.setFont(CSS.set_font())
        self.btn_pushButton_new_car.setObjectName("btn_pushButton_new_car")

        self.btn_pushButton_print_order = QtWidgets.QPushButton(self.frame)
        self.btn_pushButton_print_order.setGeometry(QtCore.QRect(443, 520, 111, 71))
        self.btn_pushButton_print_order.setAutoFillBackground(False)
        # self.btn_pushButton_print_order.setStyleSheet(CSS.set_btn_color())
        # self.btn_pushButton_print_order.setFont(CSS.set_font())
        self.btn_pushButton_print_order.setObjectName("btn_pushButton_print_order")

    def set_check_box(self):
        self.checkBox_1_repair_request = QtWidgets.QCheckBox(self.frame)
        self.checkBox_1_repair_request.setGeometry(QtCore.QRect(100, 480, 300, 21))
        # self.checkBox_1_repair_request.setFont(CSS.set_font())
        self.checkBox_1_repair_request.setAutoFillBackground(False)
        self.checkBox_1_repair_request.setChecked(True)
        self.checkBox_1_repair_request.setObjectName("checkBox_1_repair_request")

        self.checkBox_2_application_order = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2_application_order.setGeometry(QtCore.QRect(100, 510, 300, 21))
        # self.checkBox_2_application_order.setFont(CSS.set_font())
        self.checkBox_2_application_order.setAutoFillBackground(False)
        self.checkBox_2_application_order.setChecked(True)
        self.checkBox_2_application_order.setObjectName("checkBox_2_application_order")

        self.checkBox_3_act_of_acceptance = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3_act_of_acceptance.setGeometry(QtCore.QRect(100, 540, 300, 21))
        # self.checkBox_3_act_of_acceptance.setFont(CSS.set_font())
        self.checkBox_3_act_of_acceptance.setAutoFillBackground(False)
        self.checkBox_3_act_of_acceptance.setChecked(True)
        self.checkBox_3_act_of_acceptance.setObjectName("checkBox_3_act_of_acceptance")

        self.checkBox_4_internal_consumption = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4_internal_consumption.setGeometry(QtCore.QRect(100, 570, 300, 21))
        # self.checkBox_4_internal_consumption.setFont(CSS.set_font())
        self.checkBox_4_internal_consumption.setAutoFillBackground(False)
        self.checkBox_4_internal_consumption.setChecked(True)
        self.checkBox_4_internal_consumption.setObjectName("checkBox_4_internal_consumption")

    @logger.logger.catch
    def set_datetime(self):
        self.frame_data = QtWidgets.QFrame(self.frame)
        self.frame_data.setGeometry(QtCore.QRect(130, 0, 421, 51))
        self.frame_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_data.setObjectName("frame_data")

        self.dateEdit = QtWidgets.QDateEdit(self.frame_data)
        self.dateEdit.setGeometry(QtCore.QRect(80, 10, 241, 37))
        # self.dateEdit.setFont(CSS.set_font(14, True, 75))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setWrapping(True)
        self.dateEdit.setFrame(True)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(3)
        self.dateEdit.setDate(datetime.now())
        self.dateEdit.setObjectName("dateEdit")

    def set_label(self):
        self.label_client_job_title = QtWidgets.QLabel(self.frame)
        self.label_client_job_title.setGeometry(QtCore.QRect(10, 150, 120, 30))
        # self.label_client_job_title.setFont(CSS.set_font(12, False, 50))
        self.label_client_job_title.setAutoFillBackground(False)
        self.label_client_job_title.setObjectName("label_client_job_title")

        self.label_client_name = QtWidgets.QLabel(self.frame)
        self.label_client_name.setGeometry(QtCore.QRect(10, 110, 120, 30))
        # self.label_client_name.setFont(CSS.set_font(12, False, 50))
        self.label_client_name.setAutoFillBackground(False)
        self.label_client_name.setObjectName("label_client_name")

        self.label_client_owner_name = QtWidgets.QLabel(self.frame)
        self.label_client_owner_name.setGeometry(QtCore.QRect(10, 190, 120, 30))
        # self.label_client_owner_name.setFont(CSS.set_font(12, False, 50))
        self.label_client_owner_name.setAutoFillBackground(False)
        self.label_client_owner_name.setObjectName("label_client_owner_name")

        self.label_order_number = QtWidgets.QLabel(self.frame)
        self.label_order_number.setGeometry(QtCore.QRect(120, 48, 101, 30))
        # self.label_order_number.setFont(CSS.set_font(14, True, 75))
        self.label_order_number.setAutoFillBackground(False)
        self.label_order_number.setObjectName("label_order_number")

        self.label_order_number_sep = QtWidgets.QLabel(self.frame)
        self.label_order_number_sep.setGeometry(QtCore.QRect(333, 48, 16, 30))
        # self.label_order_number_sep.setFont(CSS.set_font(14, True, 75))
        self.label_order_number_sep.setAutoFillBackground(False)
        self.label_order_number_sep.setAlignment(QtCore.Qt.AlignCenter)
        self.label_order_number_sep.setObjectName("label_order_number_sep")

        self.label_client_identification_number = QtWidgets.QLabel(self.frame)
        self.label_client_identification_number.setGeometry(QtCore.QRect(10, 230, 120, 30))
        # self.label_client_identification_number.setFont(CSS.set_font(12, False, 50))
        self.label_client_identification_number.setAutoFillBackground(False)
        self.label_client_identification_number.setObjectName("label_client_identification_number")

        # CSS.line_tab(self.frame)
        # CSS.set_label_car(self.frame)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        # query = APIAxiomDB()

        self.btn_pushButton_refresh.setText(_translate("MainWindow", "Очистить"))
        self.btn_pushButton_car_car_choice.setText(_translate("MainWindow", "Машина"))
        self.btn_pushButton_new_car.setText(_translate("MainWindow", "Новая\nмашина"))
        self.btn_pushButton_print_order.setText(_translate("MainWindow", "Распечатать"))
        self.btn_pushButton_new_client.setText(_translate("MainWindow", "Новый\nклиент"))
        self.btn_pushButton_car_part_choice.setText(_translate("MainWindow", "Запчасти"))
        self.btn_pushButton_order_close.setText(_translate("MainWindow", "Закрыть Акт"))

        # self.txt_label_order_number.setText(_translate("MainWindow", str(query.count_act() + 1)))
        self.txt_label_order_number_prefix.setText(_translate("MainWindow", "А"))
        self.txt_label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.txt_label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
        # self.txt_edit_lineEdit_client_owner_name.setText(_translate("MainWindow", ""))
        # self.txt_edit_lineEdit_client_job_title.setText(_translate("MainWindow", ""))
        self.txt_label_brand.setText(_translate("MainWindow", "марка машины"))
        self.txt_label_model.setText(_translate("MainWindow", "модель машины"))
        self.txt_label_car_number.setText(_translate("MainWindow", "номер машины"))
        self.txt_label_vin_code.setText(_translate("MainWindow", "VIN код машины"))

        self.checkBox_1_repair_request.setText(_translate("MainWindow", " -  Заявка - Заказ на ремонт"))
        self.checkBox_2_application_order.setText(_translate("MainWindow", " -  Заявка - Заказ"))
        self.checkBox_3_act_of_acceptance.setText(_translate("MainWindow", " -  Акт приёмки-сдачи"))
        self.checkBox_4_internal_consumption.setText(_translate("MainWindow", " -  Внутренняя накладная"))

        self.label_order_number.setText(_translate("MainWindow", "Заявка №"))
        self.label_order_number_sep.setText(_translate("MainWindow", "-"))
        self.label_client_name.setText(_translate("MainWindow", "Клиент"))
        self.label_client_identification_number.setText(_translate("MainWindow", "УНП клиента"))
        self.label_client_owner_name.setText(_translate("MainWindow", "ФИО заказчика"))
        self.label_client_job_title.setText(_translate("MainWindow", "Должность"))

        self.dateEdit.setDisplayFormat(_translate("MainWindow", "d - MMMM - yyyy"))


if __name__ == '__main__':
    pass
