---
type: Jurisdiction
title: "Marathon County, WI"
classification: county
fips: "55073"
state: "WI"
demographics:
  population: 138403
  population_under_18: 31130
  population_18_64: 80720
  population_65_plus: 26553
  median_household_income: 77884
  poverty_rate: 8.7
  homeownership_rate: 73.3
  unemployment_rate: 2.87
  median_home_value: 219600
  gini_index: 0.4166
  vacancy_rate: 5.0
  race_white: 120384
  race_black: 800
  race_asian: 7850
  race_native: 251
  hispanic: 4893
  bachelors_plus: 35449
districts:
  - to: "us/states/wi/districts/07"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wi/districts/senate/29"
    rel: in-district
    area_weight: 0.6213
  - to: "us/states/wi/districts/senate/23"
    rel: in-district
    area_weight: 0.1992
  - to: "us/states/wi/districts/senate/12"
    rel: in-district
    area_weight: 0.1795
  - to: "us/states/wi/districts/house/86"
    rel: in-district
    area_weight: 0.2879
  - to: "us/states/wi/districts/house/87"
    rel: in-district
    area_weight: 0.2786
  - to: "us/states/wi/districts/house/69"
    rel: in-district
    area_weight: 0.1992
  - to: "us/states/wi/districts/house/35"
    rel: in-district
    area_weight: 0.1795
  - to: "us/states/wi/districts/house/85"
    rel: in-district
    area_weight: 0.0547
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Marathon County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 138403 |
| Under 18 | 31130 |
| 18–64 | 80720 |
| 65+ | 26553 |
| Median household income | 77884 |
| Poverty rate | 8.7 |
| Homeownership rate | 73.3 |
| Unemployment rate | 2.87 |
| Median home value | 219600 |
| Gini index | 0.4166 |
| Vacancy rate | 5.0 |
| White | 120384 |
| Black | 800 |
| Asian | 7850 |
| Native | 251 |
| Hispanic/Latino | 4893 |
| Bachelor's or higher | 35449 |

## Districts

- [WI-07](/us/states/wi/districts/07.md) — 100% (congressional)
- [WI Senate District 29](/us/states/wi/districts/senate/29.md) — 62% (state senate)
- [WI Senate District 23](/us/states/wi/districts/senate/23.md) — 20% (state senate)
- [WI Senate District 12](/us/states/wi/districts/senate/12.md) — 18% (state senate)
- [WI House District 86](/us/states/wi/districts/house/86.md) — 29% (state house)
- [WI House District 87](/us/states/wi/districts/house/87.md) — 28% (state house)
- [WI House District 69](/us/states/wi/districts/house/69.md) — 20% (state house)
- [WI House District 35](/us/states/wi/districts/house/35.md) — 18% (state house)
- [WI House District 85](/us/states/wi/districts/house/85.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
