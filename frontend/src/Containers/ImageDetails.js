import React from "react";
import { View, Image } from "react-native";
import { Table, Row } from "react-native-table-component";
import { images, icons, COLORS, FONTS, SIZES } from "../../constant/";

export default function ImageDetails({ route }) {
  return (
    <View>
      <View style={{ height: "40%", alignItems: "center", justifyContent: "center", backgroundColor: COLORS.white }}>
        <Image source={{ uri: route.params.uri }} style={{ resizeMode: "contain", width: "75%", height: "90%" }} />
      </View>
      <View style={{ height: "60%", backgroundColor: COLORS.white, padding: SIZES.padding }}>
        <Table style={{ backgroundColor: COLORS.white }} borderStyle={{ borderWidth: 1, borderColor: COLORS.black }}>
          <Row flexArr={[1.2, 2]} data={[" 申請案號", " " + route.params.metadatas.caseno]} />
          <Row flexArr={[1.2, 2]} data={[" 商標名稱", " " + route.params.metadatas.trademark_name]} />
          <Row flexArr={[1.2, 2]} data={[" 權利期間(起)", " " + route.params.metadatas.sdate]} />
          <Row flexArr={[1.2, 2]} data={[" 權利期間(迄)", " " + route.params.metadatas.edate]} />
          <Row flexArr={[1.2, 2]} data={[" 代理人-中文名字", " " + route.params.metadatas.bchinese]} />
          {/* <Row flexArr={[1, 2]} data={["註冊之商品與服務類別", route.params.metadatas.class]} /> */}
          <Row flexArr={[1.2, 2]} data={[" 商標權人-中文名字", " " + route.params.metadatas.achinese]} />
          <Row flexArr={[1.2, 2]} data={[" 商標權人-英文名字", " " + route.params.metadatas.aenglish]} />
          <Row flexArr={[1.2, 2]} data={[" 商標權人-地址", " " + route.params.metadatas.address]} />
        </Table>
      </View>
    </View>
  );
}
