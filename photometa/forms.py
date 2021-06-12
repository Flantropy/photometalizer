from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.forms import Form, ModelForm, FileInput
from django.forms.fields import *
from .models import Image
from exif import WhiteBalance


def validate_image_size(image: InMemoryUploadedFile):
    print(image.size)
    file_size = image.size
    limit = 10 * 1024 * 1024  # 10M
    if file_size > limit:
        raise ValidationError(f'Максимальный размер файла {limit // (1024 * 1024)}M')


class ImageUploadForm(ModelForm):
    ALLOWED_EXTENSIONS = ['jpg', 'jpeg']
    img = ImageField(
        label='Фото',
        widget=FileInput(attrs={'multiple': True}),
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS),
            validate_image_size
        ],
        help_text=f'Доступные расщирения: {ALLOWED_EXTENSIONS}',
    )

    class Meta:
        model = Image
        fields = ['img']


class ExifEditorForm(Form):
    make = CharField(help_text='Hint', required=False)
    white_balance = TypedChoiceField(
        coerce=int,
        choices=[(x.value, x.name) for x in WhiteBalance],
        help_text='Hint',
        required=False)
    # x_resolution = FloatField(help_text='Hint', required=False)
    # y_resolution = FloatField(help_text='Hint', required=False)
    # image_width = IntegerField(help_text='ширина изображения', required=False)
    # image_height = IntegerField(help_text='высота изображиния', required=False)
    # bits_per_sample = CharField(help_text='Hint', required=False)
    # compression = CharField(help_text='Hint', required=False)
    # photometric_interpretation = CharField(help_text='Hint', required=False)
    # orientation = CharField(help_text='Hint', required=False)
    # samples_per_pixel = CharField(help_text='Hint', required=False)
    # planar_configuration = CharField(help_text='Hint', required=False)
    # subsampling_ratio_of_y_to_c = CharField(help_text='Hint', required=False)
    # y_and_c_positioning = CharField(help_text='Hint', required=False)
    # resolution_unit = CharField(help_text='Hint', required=False)
    # strip_offsets = CharField(help_text='Hint', required=False)
    # rows_per_strip = CharField(help_text='Hint', required=False)
    # strip_byte_counts = CharField(help_text='Hint', required=False)
    # jpeg_interchange_format = CharField(help_text='Hint', required=False)
    # jpeg_interchange_format_length = CharField(help_text='Hint', required=False)
    # transfer_function = CharField(help_text='Hint', required=False)
    # white_point = CharField(help_text='Hint', required=False)
    # primary_chromaticities = CharField(help_text='Hint', required=False)
    # matrix_coefficients = CharField(help_text='Hint', required=False)
    # reference_black_white = CharField(help_text='Hint', required=False)
    # datetime = CharField(help_text='Hint', required=False)
    # image_description = CharField(help_text='Hint', required=False)
    # model = CharField(help_text='Hint', required=False)
    # software = CharField(help_text='Hint', required=False)
    # artist = CharField(help_text='Hint', required=False)
    # copyright = CharField(help_text='Hint', required=False)
    # exposure_time = CharField(help_text='Hint', required=False)
    # f_number = CharField(help_text='Hint', required=False)
    # exposure_program = CharField(help_text='Hint', required=False)
    # spectral_sensitivity = CharField(help_text='Hint', required=False)
    # photographic_sensitivity = CharField(help_text='Hint', required=False)
    # oecf = CharField(help_text='Hint', required=False)
    # sensitivity_type = CharField(help_text='Hint', required=False)
    # standard_output_sensitivity = CharField(help_text='Hint', required=False)
    # recommended_exposure_index = CharField(help_text='Hint', required=False)
    # iso_speed = CharField(help_text='Hint', required=False)
    # iso_speed_latitude_yyy = CharField(help_text='Hint', required=False)
    # iso_speed_latitude_zzz = CharField(help_text='Hint', required=False)
    # exif_version = CharField(help_text='Hint', required=False)
    # datetime_original = CharField(help_text='Hint', required=False)
    # datetime_digitized = CharField(help_text='Hint', required=False)
    # offset_time = CharField(help_text='Hint', required=False)
    # offset_time_original = CharField(help_text='Hint', required=False)
    # offset_time_digitized = CharField(help_text='Hint', required=False)
    # components_configuration = CharField(help_text='Hint', required=False)
    # compressed_bits_per_pixel = CharField(help_text='Hint', required=False)
    # shutter_speed_value = CharField(help_text='Hint', required=False)
    # aperture_value = CharField(help_text='Hint', required=False)
    # brightness_value = CharField(help_text='Hint', required=False)
    # exposure_bias_value = CharField(help_text='Hint', required=False)
    # max_aperture_value = CharField(help_text='Hint', required=False)
    # subject_distance = CharField(help_text='Hint', required=False)
    # metering_mode = CharField(help_text='Hint', required=False)
    # light_source = CharField(help_text='Hint', required=False)
    # flash = CharField(help_text='Hint', required=False)
    # focal_length = CharField(help_text='Hint', required=False)
    # subject_area = CharField(help_text='Hint', required=False)
    # maker_note = CharField(help_text='Hint', required=False)
    # user_comment = CharField(help_text='Hint', required=False)
    # subsec_time = CharField(help_text='Hint', required=False)
    # subsec_time_original = CharField(help_text='Hint', required=False)
    # subsec_time_digitized = CharField(help_text='Hint', required=False)
    # temperature = CharField(help_text='Hint', required=False)
    # humidity = CharField(help_text='Hint', required=False)
    # pressure = CharField(help_text='Hint', required=False)
    # water_depth = CharField(help_text='Hint', required=False)
    # acceleration = CharField(help_text='Hint', required=False)
    # camera_elevation_angle = CharField(help_text='Hint', required=False)
    # xp_title = CharField(help_text='Hint', required=False)
    # xp_comment = CharField(help_text='Hint', required=False)
    # xp_author = CharField(help_text='Hint', required=False)
    # xp_keywords = CharField(help_text='Hint', required=False)
    # xp_subject = CharField(help_text='Hint', required=False)
    # flashpix_version = CharField(help_text='Hint', required=False)
    # color_space = CharField(help_text='Hint', required=False)
    # pixel_x_dimension = CharField(help_text='Hint', required=False)
    # pixel_y_dimension = CharField(help_text='Hint', required=False)
    # related_sound_file = CharField(help_text='Hint', required=False)
    # flash_energy = CharField(help_text='Hint', required=False)
    # spatial_frequency_response = CharField(help_text='Hint', required=False)
    # focal_plane_x_resolution = CharField(help_text='Hint', required=False)
    # focal_plane_y_resolution = CharField(help_text='Hint', required=False)
    # focal_plane_resolution_unit = CharField(help_text='Hint', required=False)
    # subject_location = CharField(help_text='Hint', required=False)
    # exposure_index = CharField(help_text='Hint', required=False)
    # sensing_method = CharField(help_text='Hint', required=False)
    # file_source = CharField(help_text='Hint', required=False)
    # scene_type = CharField(help_text='Hint', required=False)
    # cfa_pattern = CharField(help_text='Hint', required=False)
    # custom_rendered = CharField(help_text='Hint', required=False)
    # exposure_mode = CharField(help_text='Hint', required=False)
    # digital_zoom_ratio = CharField(help_text='Hint', required=False)
    # focal_length_in_35mm_film = CharField(help_text='Hint', required=False)
    # scene_capture_type = CharField(help_text='Hint', required=False)
    # gain_control = CharField(help_text='Hint', required=False)
    # contrast = CharField(help_text='Hint', required=False)
    # saturation = CharField(help_text='Hint', required=False)
    # sharpness = CharField(help_text='Hint', required=False)
    # device_setting_description = CharField(help_text='Hint', required=False)
    # subject_distance_range = CharField(help_text='Hint', required=False)
    # image_unique_id = CharField(help_text='Hint', required=False)
    # camera_owner_name = CharField(help_text='Hint', required=False)
    # body_serial_number = CharField(help_text='Hint', required=False)
    # lens_specification = CharField(help_text='Hint', required=False)
    # lens_make = CharField(help_text='Hint', required=False)
    # lens_model = CharField(help_text='Hint', required=False)
    # lens_serial_number = CharField(help_text='Hint', required=False)
    # gamma = CharField(help_text='Hint', required=False)
    # gps_version_id = CharField(help_text='Hint', required=False)
    # gps_latitude_ref = CharField(help_text='Hint', required=False)
    # gps_latitude = CharField(help_text='Hint', required=False)
    # gps_longitude_ref = CharField(help_text='Hint', required=False)
    # gps_longitude = CharField(help_text='Hint', required=False)
    # gps_altitude_ref = CharField(help_text='Hint', required=False)
    # gps_altitude = CharField(help_text='Hint', required=False)
    # gps_timestamp = CharField(help_text='Hint', required=False)
    # gps_satellites = CharField(help_text='Hint', required=False)
    # gps_status = CharField(help_text='Hint', required=False)
    # gps_measure_mode = CharField(help_text='Hint', required=False)
    # gps_dop = CharField(help_text='Hint', required=False)
    # gps_speed_ref = CharField(help_text='Hint', required=False)
    # gps_speed = CharField(help_text='Hint', required=False)
    # gps_track_ref = CharField(help_text='Hint', required=False)
    # gps_track = CharField(help_text='Hint', required=False)
    # gps_img_direction_ref = CharField(help_text='Hint', required=False)
    # gps_img_direction = CharField(help_text='Hint', required=False)
    # gps_map_datum = CharField(help_text='Hint', required=False)
    # gps_dest_latitude_ref = CharField(help_text='Hint', required=False)
    # gps_dest_latitude = CharField(help_text='Hint', required=False)
    # gps_dest_longitude_ref = CharField(help_text='Hint', required=False)
    # gps_dest_longitude = CharField(help_text='Hint', required=False)
    # gps_dest_bearing_ref = CharField(help_text='Hint', required=False)
    # gps_dest_bearing = CharField(help_text='Hint', required=False)
    # gps_dest_distance_ref = CharField(help_text='Hint', required=False)
    # gps_dest_distance = CharField(help_text='Hint', required=False)
    # gps_processing_method = CharField(help_text='Hint', required=False)
    # gps_area_information = CharField(help_text='Hint', required=False)
    # gps_datestamp = CharField(help_text='Hint', required=False)
    # gps_differential = CharField(help_text='Hint', required=False)
    # gps_horizontal_positioning_error = CharField(help_text='Hint', required=False)
