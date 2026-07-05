---
type: Jurisdiction
title: "Albany County, WY"
classification: county
fips: "56001"
state: "WY"
demographics:
  population: 38249
  population_under_18: 5887
  population_18_64: 27193
  population_65_plus: 5169
  median_household_income: 61917
  poverty_rate: 20.89
  homeownership_rate: 50.03
  unemployment_rate: 3.75
  median_home_value: 333000
  gini_index: 0.4674
  vacancy_rate: 9.38
  race_white: 31971
  race_black: 429
  race_asian: 1395
  race_native: 300
  hispanic: 4043
  bachelors_plus: 17886
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/10"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/wy/districts/house/14"
    rel: in-district
    area_weight: 0.6309
  - to: "us/states/wy/districts/house/46"
    rel: in-district
    area_weight: 0.3674
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Albany County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38249 |
| Under 18 | 5887 |
| 18–64 | 27193 |
| 65+ | 5169 |
| Median household income | 61917 |
| Poverty rate | 20.89 |
| Homeownership rate | 50.03 |
| Unemployment rate | 3.75 |
| Median home value | 333000 |
| Gini index | 0.4674 |
| Vacancy rate | 9.38 |
| White | 31971 |
| Black | 429 |
| Asian | 1395 |
| Native | 300 |
| Hispanic/Latino | 4043 |
| Bachelor's or higher | 17886 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 10](/us/states/wy/districts/senate/10.md) — 100% (state senate)
- [WY House District 14](/us/states/wy/districts/house/14.md) — 63% (state house)
- [WY House District 46](/us/states/wy/districts/house/46.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
