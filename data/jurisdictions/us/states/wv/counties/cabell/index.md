---
type: Jurisdiction
title: "Cabell County, WV"
classification: county
fips: "54011"
state: "WV"
demographics:
  population: 92739
  population_under_18: 18285
  population_18_64: 55904
  population_65_plus: 18550
  median_household_income: 55832
  poverty_rate: 19.2
  homeownership_rate: 64.18
  unemployment_rate: 5.13
  median_home_value: 164400
  gini_index: 0.5068
  vacancy_rate: 14.58
  race_white: 82935
  race_black: 3947
  race_asian: 1075
  race_native: 50
  hispanic: 1631
  bachelors_plus: 28564
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/senate/4"
    rel: in-district
    area_weight: 0.5678
  - to: "us/states/wv/districts/senate/5"
    rel: in-district
    area_weight: 0.4317
  - to: "us/states/wv/districts/house/22"
    rel: in-district
    area_weight: 0.5009
  - to: "us/states/wv/districts/house/23"
    rel: in-district
    area_weight: 0.2598
  - to: "us/states/wv/districts/house/26"
    rel: in-district
    area_weight: 0.0945
  - to: "us/states/wv/districts/house/24"
    rel: in-district
    area_weight: 0.0734
  - to: "us/states/wv/districts/house/27"
    rel: in-district
    area_weight: 0.0551
  - to: "us/states/wv/districts/house/25"
    rel: in-district
    area_weight: 0.0156
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Cabell County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92739 |
| Under 18 | 18285 |
| 18–64 | 55904 |
| 65+ | 18550 |
| Median household income | 55832 |
| Poverty rate | 19.2 |
| Homeownership rate | 64.18 |
| Unemployment rate | 5.13 |
| Median home value | 164400 |
| Gini index | 0.5068 |
| Vacancy rate | 14.58 |
| White | 82935 |
| Black | 3947 |
| Asian | 1075 |
| Native | 50 |
| Hispanic/Latino | 1631 |
| Bachelor's or higher | 28564 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 4](/us/states/wv/districts/senate/4.md) — 57% (state senate)
- [WV Senate District 5](/us/states/wv/districts/senate/5.md) — 43% (state senate)
- [WV House District 22](/us/states/wv/districts/house/22.md) — 50% (state house)
- [WV House District 23](/us/states/wv/districts/house/23.md) — 26% (state house)
- [WV House District 26](/us/states/wv/districts/house/26.md) — 9% (state house)
- [WV House District 24](/us/states/wv/districts/house/24.md) — 7% (state house)
- [WV House District 27](/us/states/wv/districts/house/27.md) — 6% (state house)
- [WV House District 25](/us/states/wv/districts/house/25.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
