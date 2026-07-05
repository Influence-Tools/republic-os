---
type: Jurisdiction
title: "Socorro County, NM"
classification: county
fips: "35053"
state: "NM"
demographics:
  population: 16200
  population_under_18: 3883
  population_18_64: 8907
  population_65_plus: 3410
  median_household_income: 36570
  poverty_rate: 33.16
  homeownership_rate: 75.1
  unemployment_rate: 1.26
  median_home_value: 137500
  gini_index: 0.5539
  vacancy_rate: 31.51
  race_white: 6842
  race_black: 64
  race_asian: 294
  race_native: 1722
  hispanic: 8155
  bachelors_plus: 2834
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.7071
  - to: "us/states/nm/districts/senate/29"
    rel: in-district
    area_weight: 0.1652
  - to: "us/states/nm/districts/senate/30"
    rel: in-district
    area_weight: 0.1277
  - to: "us/states/nm/districts/house/49"
    rel: in-district
    area_weight: 0.7078
  - to: "us/states/nm/districts/house/38"
    rel: in-district
    area_weight: 0.2217
  - to: "us/states/nm/districts/house/69"
    rel: in-district
    area_weight: 0.0705
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Socorro County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16200 |
| Under 18 | 3883 |
| 18–64 | 8907 |
| 65+ | 3410 |
| Median household income | 36570 |
| Poverty rate | 33.16 |
| Homeownership rate | 75.1 |
| Unemployment rate | 1.26 |
| Median home value | 137500 |
| Gini index | 0.5539 |
| Vacancy rate | 31.51 |
| White | 6842 |
| Black | 64 |
| Asian | 294 |
| Native | 1722 |
| Hispanic/Latino | 8155 |
| Bachelor's or higher | 2834 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 71% (state senate)
- [NM Senate District 29](/us/states/nm/districts/senate/29.md) — 17% (state senate)
- [NM Senate District 30](/us/states/nm/districts/senate/30.md) — 13% (state senate)
- [NM House District 49](/us/states/nm/districts/house/49.md) — 71% (state house)
- [NM House District 38](/us/states/nm/districts/house/38.md) — 22% (state house)
- [NM House District 69](/us/states/nm/districts/house/69.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
