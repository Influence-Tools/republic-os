---
type: Jurisdiction
title: "Washington County, RI"
classification: county
fips: "44009"
state: "RI"
demographics:
  population: 130344
  population_under_18: 20042
  population_18_64: 79880
  population_65_plus: 30422
  median_household_income: 106638
  poverty_rate: 8.19
  homeownership_rate: 77.53
  unemployment_rate: 4.42
  median_home_value: 510800
  gini_index: 0.4397
  vacancy_rate: 20.84
  race_white: 116802
  race_black: 1738
  race_asian: 2844
  race_native: 490
  hispanic: 4968
  bachelors_plus: 69499
districts:
  - to: "us/states/ri/districts/02"
    rel: in-district
    area_weight: 0.6241
  - to: "us/states/ri/districts/senate/34"
    rel: in-district
    area_weight: 0.2922
  - to: "us/states/ri/districts/senate/38"
    rel: in-district
    area_weight: 0.1023
  - to: "us/states/ri/districts/senate/37"
    rel: in-district
    area_weight: 0.0967
  - to: "us/states/ri/districts/senate/36"
    rel: in-district
    area_weight: 0.0903
  - to: "us/states/ri/districts/senate/35"
    rel: in-district
    area_weight: 0.044
  - to: "us/states/ri/districts/house/39"
    rel: in-district
    area_weight: 0.1838
  - to: "us/states/ri/districts/house/36"
    rel: in-district
    area_weight: 0.1304
  - to: "us/states/ri/districts/house/38"
    rel: in-district
    area_weight: 0.0741
  - to: "us/states/ri/districts/house/35"
    rel: in-district
    area_weight: 0.0555
  - to: "us/states/ri/districts/house/32"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/ri/districts/house/31"
    rel: in-district
    area_weight: 0.0447
  - to: "us/states/ri/districts/house/33"
    rel: in-district
    area_weight: 0.034
  - to: "us/states/ri/districts/house/37"
    rel: in-district
    area_weight: 0.031
  - to: "us/states/ri/districts/house/34"
    rel: in-district
    area_weight: 0.0261
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ri]
timestamp: "2026-07-03"
---

# Washington County, RI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 130344 |
| Under 18 | 20042 |
| 18–64 | 79880 |
| 65+ | 30422 |
| Median household income | 106638 |
| Poverty rate | 8.19 |
| Homeownership rate | 77.53 |
| Unemployment rate | 4.42 |
| Median home value | 510800 |
| Gini index | 0.4397 |
| Vacancy rate | 20.84 |
| White | 116802 |
| Black | 1738 |
| Asian | 2844 |
| Native | 490 |
| Hispanic/Latino | 4968 |
| Bachelor's or higher | 69499 |

## Districts

- [RI-02](/us/states/ri/districts/02.md) — 62% (congressional)
- [RI Senate District 34](/us/states/ri/districts/senate/34.md) — 29% (state senate)
- [RI Senate District 38](/us/states/ri/districts/senate/38.md) — 10% (state senate)
- [RI Senate District 37](/us/states/ri/districts/senate/37.md) — 10% (state senate)
- [RI Senate District 36](/us/states/ri/districts/senate/36.md) — 9% (state senate)
- [RI Senate District 35](/us/states/ri/districts/senate/35.md) — 4% (state senate)
- [RI House District 39](/us/states/ri/districts/house/39.md) — 18% (state house)
- [RI House District 36](/us/states/ri/districts/house/36.md) — 13% (state house)
- [RI House District 38](/us/states/ri/districts/house/38.md) — 7% (state house)
- [RI House District 35](/us/states/ri/districts/house/35.md) — 6% (state house)
- [RI House District 32](/us/states/ri/districts/house/32.md) — 5% (state house)
- [RI House District 31](/us/states/ri/districts/house/31.md) — 4% (state house)
- [RI House District 33](/us/states/ri/districts/house/33.md) — 3% (state house)
- [RI House District 37](/us/states/ri/districts/house/37.md) — 3% (state house)
- [RI House District 34](/us/states/ri/districts/house/34.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
