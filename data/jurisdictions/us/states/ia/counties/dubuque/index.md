---
type: Jurisdiction
title: "Dubuque County, IA"
classification: county
fips: "19061"
state: "IA"
demographics:
  population: 99030
  population_under_18: 22317
  population_18_64: 57561
  population_65_plus: 19152
  median_household_income: 77630
  poverty_rate: 9.65
  homeownership_rate: 73.34
  unemployment_rate: 3.66
  median_home_value: 237300
  gini_index: 0.4429
  vacancy_rate: 5.31
  race_white: 88050
  race_black: 2932
  race_asian: 1354
  race_native: 39
  hispanic: 3234
  bachelors_plus: 30135
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ia/districts/senate/33"
    rel: in-district
    area_weight: 0.7612
  - to: "us/states/ia/districts/senate/36"
    rel: in-district
    area_weight: 0.1194
  - to: "us/states/ia/districts/senate/34"
    rel: in-district
    area_weight: 0.06
  - to: "us/states/ia/districts/senate/32"
    rel: in-district
    area_weight: 0.0593
  - to: "us/states/ia/districts/house/65"
    rel: in-district
    area_weight: 0.7611
  - to: "us/states/ia/districts/house/72"
    rel: in-district
    area_weight: 0.0972
  - to: "us/states/ia/districts/house/67"
    rel: in-district
    area_weight: 0.06
  - to: "us/states/ia/districts/house/64"
    rel: in-district
    area_weight: 0.0593
  - to: "us/states/ia/districts/house/71"
    rel: in-district
    area_weight: 0.0222
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Dubuque County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99030 |
| Under 18 | 22317 |
| 18–64 | 57561 |
| 65+ | 19152 |
| Median household income | 77630 |
| Poverty rate | 9.65 |
| Homeownership rate | 73.34 |
| Unemployment rate | 3.66 |
| Median home value | 237300 |
| Gini index | 0.4429 |
| Vacancy rate | 5.31 |
| White | 88050 |
| Black | 2932 |
| Asian | 1354 |
| Native | 39 |
| Hispanic/Latino | 3234 |
| Bachelor's or higher | 30135 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 33](/us/states/ia/districts/senate/33.md) — 76% (state senate)
- [IA Senate District 36](/us/states/ia/districts/senate/36.md) — 12% (state senate)
- [IA Senate District 34](/us/states/ia/districts/senate/34.md) — 6% (state senate)
- [IA Senate District 32](/us/states/ia/districts/senate/32.md) — 6% (state senate)
- [IA House District 65](/us/states/ia/districts/house/65.md) — 76% (state house)
- [IA House District 72](/us/states/ia/districts/house/72.md) — 10% (state house)
- [IA House District 67](/us/states/ia/districts/house/67.md) — 6% (state house)
- [IA House District 64](/us/states/ia/districts/house/64.md) — 6% (state house)
- [IA House District 71](/us/states/ia/districts/house/71.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
