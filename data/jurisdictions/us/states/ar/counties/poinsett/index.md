---
type: Jurisdiction
title: "Poinsett County, AR"
classification: county
fips: "05111"
state: "AR"
demographics:
  population: 22543
  population_under_18: 5455
  population_18_64: 12918
  population_65_plus: 4170
  median_household_income: 46707
  poverty_rate: 20.1
  homeownership_rate: 64.44
  unemployment_rate: 6.38
  median_home_value: 103000
  gini_index: 0.4711
  vacancy_rate: 15.86
  race_white: 19058
  race_black: 1206
  race_asian: 41
  race_native: 109
  hispanic: 859
  bachelors_plus: 2293
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/19"
    rel: in-district
    area_weight: 0.7798
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.2202
  - to: "us/states/ar/districts/house/37"
    rel: in-district
    area_weight: 0.407
  - to: "us/states/ar/districts/house/38"
    rel: in-district
    area_weight: 0.4024
  - to: "us/states/ar/districts/house/36"
    rel: in-district
    area_weight: 0.1905
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Poinsett County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22543 |
| Under 18 | 5455 |
| 18–64 | 12918 |
| 65+ | 4170 |
| Median household income | 46707 |
| Poverty rate | 20.1 |
| Homeownership rate | 64.44 |
| Unemployment rate | 6.38 |
| Median home value | 103000 |
| Gini index | 0.4711 |
| Vacancy rate | 15.86 |
| White | 19058 |
| Black | 1206 |
| Asian | 41 |
| Native | 109 |
| Hispanic/Latino | 859 |
| Bachelor's or higher | 2293 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 19](/us/states/ar/districts/senate/19.md) — 78% (state senate)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 22% (state senate)
- [AR House District 37](/us/states/ar/districts/house/37.md) — 41% (state house)
- [AR House District 38](/us/states/ar/districts/house/38.md) — 40% (state house)
- [AR House District 36](/us/states/ar/districts/house/36.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
