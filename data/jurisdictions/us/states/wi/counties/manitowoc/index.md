---
type: Jurisdiction
title: "Manitowoc County, WI"
classification: county
fips: "55071"
state: "WI"
demographics:
  population: 81406
  population_under_18: 16492
  population_18_64: 46796
  population_65_plus: 18118
  median_household_income: 69148
  poverty_rate: 9.55
  homeownership_rate: 77.1
  unemployment_rate: 2.6
  median_home_value: 186900
  gini_index: 0.4105
  vacancy_rate: 7.6
  race_white: 71911
  race_black: 620
  race_asian: 1964
  race_native: 172
  hispanic: 4474
  bachelors_plus: 17258
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.3987
  - to: "us/states/wi/districts/senate/1"
    rel: in-district
    area_weight: 0.2504
  - to: "us/states/wi/districts/senate/9"
    rel: in-district
    area_weight: 0.1481
  - to: "us/states/wi/districts/house/2"
    rel: in-district
    area_weight: 0.1541
  - to: "us/states/wi/districts/house/25"
    rel: in-district
    area_weight: 0.1242
  - to: "us/states/wi/districts/house/3"
    rel: in-district
    area_weight: 0.0962
  - to: "us/states/wi/districts/house/27"
    rel: in-district
    area_weight: 0.024
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Manitowoc County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 81406 |
| Under 18 | 16492 |
| 18–64 | 46796 |
| 65+ | 18118 |
| Median household income | 69148 |
| Poverty rate | 9.55 |
| Homeownership rate | 77.1 |
| Unemployment rate | 2.6 |
| Median home value | 186900 |
| Gini index | 0.4105 |
| Vacancy rate | 7.6 |
| White | 71911 |
| Black | 620 |
| Asian | 1964 |
| Native | 172 |
| Hispanic/Latino | 4474 |
| Bachelor's or higher | 17258 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 40% (congressional)
- [WI Senate District 1](/us/states/wi/districts/senate/1.md) — 25% (state senate)
- [WI Senate District 9](/us/states/wi/districts/senate/9.md) — 15% (state senate)
- [WI House District 2](/us/states/wi/districts/house/2.md) — 15% (state house)
- [WI House District 25](/us/states/wi/districts/house/25.md) — 12% (state house)
- [WI House District 3](/us/states/wi/districts/house/3.md) — 10% (state house)
- [WI House District 27](/us/states/wi/districts/house/27.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
