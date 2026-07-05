---
type: Jurisdiction
title: "Franklin County, IL"
classification: county
fips: "17055"
state: "IL"
demographics:
  population: 37323
  population_under_18: 8240
  population_18_64: 21248
  population_65_plus: 7835
  median_household_income: 56740
  poverty_rate: 17.51
  homeownership_rate: 74.13
  unemployment_rate: 7.66
  median_home_value: 89000
  gini_index: 0.4563
  vacancy_rate: 12.59
  race_white: 35347
  race_black: 154
  race_asian: 131
  race_native: 29
  hispanic: 756
  bachelors_plus: 5501
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.5494
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.5492
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.4505
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Franklin County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37323 |
| Under 18 | 8240 |
| 18–64 | 21248 |
| 65+ | 7835 |
| Median household income | 56740 |
| Poverty rate | 17.51 |
| Homeownership rate | 74.13 |
| Unemployment rate | 7.66 |
| Median home value | 89000 |
| Gini index | 0.4563 |
| Vacancy rate | 12.59 |
| White | 35347 |
| Black | 154 |
| Asian | 131 |
| Native | 29 |
| Hispanic/Latino | 756 |
| Bachelor's or higher | 5501 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 55% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 55% (state house)
- [IL House District 117](/us/states/il/districts/house/117.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
