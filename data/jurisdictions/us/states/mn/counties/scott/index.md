---
type: Jurisdiction
title: "Scott County, MN"
classification: county
fips: "27139"
state: "MN"
demographics:
  population: 154557
  population_under_18: 39951
  population_18_64: 94991
  population_65_plus: 19615
  median_household_income: 119314
  poverty_rate: 4.6
  homeownership_rate: 83.81
  unemployment_rate: 3.46
  median_home_value: 419400
  gini_index: 0.4116
  vacancy_rate: 3.0
  race_white: 119221
  race_black: 9507
  race_asian: 9835
  race_native: 1103
  hispanic: 9930
  bachelors_plus: 58126
districts:
  - to: "us/states/mn/districts/02"
    rel: in-district
    area_weight: 0.9925
  - to: "us/states/mn/districts/senate/54"
    rel: in-district
    area_weight: 0.3644
  - to: "us/states/mn/districts/senate/22"
    rel: in-district
    area_weight: 0.2318
  - to: "us/states/mn/districts/senate/58"
    rel: in-district
    area_weight: 0.1966
  - to: "us/states/mn/districts/senate/57"
    rel: in-district
    area_weight: 0.1619
  - to: "us/states/mn/districts/senate/55"
    rel: in-district
    area_weight: 0.0446
  - to: "us/states/mn/districts/house/54b"
    rel: in-district
    area_weight: 0.2849
  - to: "us/states/mn/districts/house/22b"
    rel: in-district
    area_weight: 0.2318
  - to: "us/states/mn/districts/house/58a"
    rel: in-district
    area_weight: 0.1966
  - to: "us/states/mn/districts/house/57a"
    rel: in-district
    area_weight: 0.1619
  - to: "us/states/mn/districts/house/54a"
    rel: in-district
    area_weight: 0.0795
  - to: "us/states/mn/districts/house/55a"
    rel: in-district
    area_weight: 0.0446
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Scott County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 154557 |
| Under 18 | 39951 |
| 18–64 | 94991 |
| 65+ | 19615 |
| Median household income | 119314 |
| Poverty rate | 4.6 |
| Homeownership rate | 83.81 |
| Unemployment rate | 3.46 |
| Median home value | 419400 |
| Gini index | 0.4116 |
| Vacancy rate | 3.0 |
| White | 119221 |
| Black | 9507 |
| Asian | 9835 |
| Native | 1103 |
| Hispanic/Latino | 9930 |
| Bachelor's or higher | 58126 |

## Districts

- [MN-02](/us/states/mn/districts/02.md) — 99% (congressional)
- [MN Senate District 54](/us/states/mn/districts/senate/54.md) — 36% (state senate)
- [MN Senate District 22](/us/states/mn/districts/senate/22.md) — 23% (state senate)
- [MN Senate District 58](/us/states/mn/districts/senate/58.md) — 20% (state senate)
- [MN Senate District 57](/us/states/mn/districts/senate/57.md) — 16% (state senate)
- [MN Senate District 55](/us/states/mn/districts/senate/55.md) — 4% (state senate)
- [MN House District 54B](/us/states/mn/districts/house/54b.md) — 28% (state house)
- [MN House District 22B](/us/states/mn/districts/house/22b.md) — 23% (state house)
- [MN House District 58A](/us/states/mn/districts/house/58a.md) — 20% (state house)
- [MN House District 57A](/us/states/mn/districts/house/57a.md) — 16% (state house)
- [MN House District 54A](/us/states/mn/districts/house/54a.md) — 8% (state house)
- [MN House District 55A](/us/states/mn/districts/house/55a.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
