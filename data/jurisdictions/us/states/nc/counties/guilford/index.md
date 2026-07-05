---
type: Jurisdiction
title: "Guilford County, NC"
classification: county
fips: "37081"
state: "NC"
demographics:
  population: 547940
  population_under_18: 120573
  population_18_64: 340183
  population_65_plus: 87184
  median_household_income: 68642
  poverty_rate: 14.58
  homeownership_rate: 59.95
  unemployment_rate: 4.57
  median_home_value: 259900
  gini_index: 0.479
  vacancy_rate: 7.69
  race_white: 260614
  race_black: 185470
  race_asian: 29591
  race_native: 1585
  hispanic: 55083
  bachelors_plus: 195459
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.5404
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.3044
  - to: "us/states/nc/districts/06"
    rel: in-district
    area_weight: 0.1553
  - to: "us/states/nc/districts/senate/26"
    rel: in-district
    area_weight: 0.6278
  - to: "us/states/nc/districts/senate/27"
    rel: in-district
    area_weight: 0.2307
  - to: "us/states/nc/districts/senate/28"
    rel: in-district
    area_weight: 0.1415
  - to: "us/states/nc/districts/house/59"
    rel: in-district
    area_weight: 0.4905
  - to: "us/states/nc/districts/house/62"
    rel: in-district
    area_weight: 0.2427
  - to: "us/states/nc/districts/house/58"
    rel: in-district
    area_weight: 0.0833
  - to: "us/states/nc/districts/house/57"
    rel: in-district
    area_weight: 0.0751
  - to: "us/states/nc/districts/house/60"
    rel: in-district
    area_weight: 0.0673
  - to: "us/states/nc/districts/house/61"
    rel: in-district
    area_weight: 0.041
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Guilford County, NC

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 547940 |
| Under 18 | 120573 |
| 18–64 | 340183 |
| 65+ | 87184 |
| Median household income | 68642 |
| Poverty rate | 14.58 |
| Homeownership rate | 59.95 |
| Unemployment rate | 4.57 |
| Median home value | 259900 |
| Gini index | 0.479 |
| Vacancy rate | 7.69 |
| White | 260614 |
| Black | 185470 |
| Asian | 29591 |
| Native | 1585 |
| Hispanic/Latino | 55083 |
| Bachelor's or higher | 195459 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 54% (congressional)
- [NC-05](/us/states/nc/districts/05.md) — 30% (congressional)
- [NC-06](/us/states/nc/districts/06.md) — 16% (congressional)
- [NC Senate District 26](/us/states/nc/districts/senate/26.md) — 63% (state senate)
- [NC Senate District 27](/us/states/nc/districts/senate/27.md) — 23% (state senate)
- [NC Senate District 28](/us/states/nc/districts/senate/28.md) — 14% (state senate)
- [NC House District 59](/us/states/nc/districts/house/59.md) — 49% (state house)
- [NC House District 62](/us/states/nc/districts/house/62.md) — 24% (state house)
- [NC House District 58](/us/states/nc/districts/house/58.md) — 8% (state house)
- [NC House District 57](/us/states/nc/districts/house/57.md) — 8% (state house)
- [NC House District 60](/us/states/nc/districts/house/60.md) — 7% (state house)
- [NC House District 61](/us/states/nc/districts/house/61.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
