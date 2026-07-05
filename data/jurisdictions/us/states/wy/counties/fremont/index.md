---
type: Jurisdiction
title: "Fremont County, WY"
classification: county
fips: "56013"
state: "WY"
demographics:
  population: 39533
  population_under_18: 9672
  population_18_64: 21958
  population_65_plus: 7903
  median_household_income: 64904
  poverty_rate: 12.82
  homeownership_rate: 70.14
  unemployment_rate: 7.4
  median_home_value: 268800
  gini_index: 0.4064
  vacancy_rate: 13.92
  race_white: 28031
  race_black: 216
  race_asian: 130
  race_native: 7233
  hispanic: 2745
  bachelors_plus: 9835
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/26"
    rel: in-district
    area_weight: 0.5547
  - to: "us/states/wy/districts/senate/25"
    rel: in-district
    area_weight: 0.2951
  - to: "us/states/wy/districts/senate/20"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/wy/districts/house/34"
    rel: in-district
    area_weight: 0.5536
  - to: "us/states/wy/districts/house/33"
    rel: in-district
    area_weight: 0.2851
  - to: "us/states/wy/districts/house/28"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/wy/districts/house/54"
    rel: in-district
    area_weight: 0.01
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Fremont County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39533 |
| Under 18 | 9672 |
| 18–64 | 21958 |
| 65+ | 7903 |
| Median household income | 64904 |
| Poverty rate | 12.82 |
| Homeownership rate | 70.14 |
| Unemployment rate | 7.4 |
| Median home value | 268800 |
| Gini index | 0.4064 |
| Vacancy rate | 13.92 |
| White | 28031 |
| Black | 216 |
| Asian | 130 |
| Native | 7233 |
| Hispanic/Latino | 2745 |
| Bachelor's or higher | 9835 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 26](/us/states/wy/districts/senate/26.md) — 55% (state senate)
- [WY Senate District 25](/us/states/wy/districts/senate/25.md) — 30% (state senate)
- [WY Senate District 20](/us/states/wy/districts/senate/20.md) — 15% (state senate)
- [WY House District 34](/us/states/wy/districts/house/34.md) — 55% (state house)
- [WY House District 33](/us/states/wy/districts/house/33.md) — 29% (state house)
- [WY House District 28](/us/states/wy/districts/house/28.md) — 15% (state house)
- [WY House District 54](/us/states/wy/districts/house/54.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
