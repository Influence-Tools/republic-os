---
type: Jurisdiction
title: "Livingston County, IL"
classification: county
fips: "17105"
state: "IL"
demographics:
  population: 35565
  population_under_18: 7802
  population_18_64: 20599
  population_65_plus: 7164
  median_household_income: 73790
  poverty_rate: 10.52
  homeownership_rate: 74.31
  unemployment_rate: 3.46
  median_home_value: 142200
  gini_index: 0.4124
  vacancy_rate: 8.25
  race_white: 31676
  race_black: 1209
  race_asian: 239
  race_native: 37
  hispanic: 2070
  bachelors_plus: 6281
districts:
  - to: "us/states/il/districts/02"
    rel: in-district
    area_weight: 0.5961
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.4039
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.9782
  - to: "us/states/il/districts/senate/44"
    rel: in-district
    area_weight: 0.0218
  - to: "us/states/il/districts/house/106"
    rel: in-district
    area_weight: 0.6635
  - to: "us/states/il/districts/house/105"
    rel: in-district
    area_weight: 0.3147
  - to: "us/states/il/districts/house/88"
    rel: in-district
    area_weight: 0.0218
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Livingston County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35565 |
| Under 18 | 7802 |
| 18–64 | 20599 |
| 65+ | 7164 |
| Median household income | 73790 |
| Poverty rate | 10.52 |
| Homeownership rate | 74.31 |
| Unemployment rate | 3.46 |
| Median home value | 142200 |
| Gini index | 0.4124 |
| Vacancy rate | 8.25 |
| White | 31676 |
| Black | 1209 |
| Asian | 239 |
| Native | 37 |
| Hispanic/Latino | 2070 |
| Bachelor's or higher | 6281 |

## Districts

- [IL-02](/us/states/il/districts/02.md) — 60% (congressional)
- [IL-16](/us/states/il/districts/16.md) — 40% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 98% (state senate)
- [IL Senate District 44](/us/states/il/districts/senate/44.md) — 2% (state senate)
- [IL House District 106](/us/states/il/districts/house/106.md) — 66% (state house)
- [IL House District 105](/us/states/il/districts/house/105.md) — 31% (state house)
- [IL House District 88](/us/states/il/districts/house/88.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
