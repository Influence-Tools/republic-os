---
type: Jurisdiction
title: "Contra Costa County, CA"
classification: county
fips: "06013"
state: "CA"
demographics:
  population: 1165012
  population_under_18: 256000
  population_18_64: 709742
  population_65_plus: 199270
  median_household_income: 127229
  poverty_rate: 8.36
  homeownership_rate: 68.0
  unemployment_rate: 6.49
  median_home_value: 866800
  gini_index: 0.4715
  vacancy_rate: 3.46
  race_white: 479110
  race_black: 96408
  race_asian: 219557
  race_native: 11438
  hispanic: 321749
  bachelors_plus: 513781
districts:
  - to: "us/states/ca/districts/10"
    rel: in-district
    area_weight: 0.6818
  - to: "us/states/ca/districts/08"
    rel: in-district
    area_weight: 0.2132
  - to: "us/states/ca/districts/09"
    rel: in-district
    area_weight: 0.0488
  - to: "us/states/ca/districts/senate/9"
    rel: in-district
    area_weight: 0.6822
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.1808
  - to: "us/states/ca/districts/senate/7"
    rel: in-district
    area_weight: 0.0826
  - to: "us/states/ca/districts/house/15"
    rel: in-district
    area_weight: 0.4314
  - to: "us/states/ca/districts/house/16"
    rel: in-district
    area_weight: 0.2897
  - to: "us/states/ca/districts/house/11"
    rel: in-district
    area_weight: 0.134
  - to: "us/states/ca/districts/house/14"
    rel: in-district
    area_weight: 0.0904
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Contra Costa County, CA

County jurisdiction — 7 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1165012 |
| Under 18 | 256000 |
| 18–64 | 709742 |
| 65+ | 199270 |
| Median household income | 127229 |
| Poverty rate | 8.36 |
| Homeownership rate | 68.0 |
| Unemployment rate | 6.49 |
| Median home value | 866800 |
| Gini index | 0.4715 |
| Vacancy rate | 3.46 |
| White | 479110 |
| Black | 96408 |
| Asian | 219557 |
| Native | 11438 |
| Hispanic/Latino | 321749 |
| Bachelor's or higher | 513781 |

## Districts

- [CA-10](/us/states/ca/districts/10.md) — 68% (congressional)
- [CA-08](/us/states/ca/districts/08.md) — 21% (congressional)
- [CA-09](/us/states/ca/districts/09.md) — 5% (congressional)
- [CA Senate District 9](/us/states/ca/districts/senate/9.md) — 68% (state senate)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 18% (state senate)
- [CA Senate District 7](/us/states/ca/districts/senate/7.md) — 8% (state senate)
- [CA House District 15](/us/states/ca/districts/house/15.md) — 43% (state house)
- [CA House District 16](/us/states/ca/districts/house/16.md) — 29% (state house)
- [CA House District 11](/us/states/ca/districts/house/11.md) — 13% (state house)
- [CA House District 14](/us/states/ca/districts/house/14.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
