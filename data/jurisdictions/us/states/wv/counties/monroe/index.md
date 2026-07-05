---
type: Jurisdiction
title: "Monroe County, WV"
classification: county
fips: "54063"
state: "WV"
demographics:
  population: 12386
  population_under_18: 2628
  population_18_64: 6648
  population_65_plus: 3110
  median_household_income: 56750
  poverty_rate: 13.97
  homeownership_rate: 86.86
  unemployment_rate: 4.77
  median_home_value: 156300
  gini_index: 0.3976
  vacancy_rate: 25.98
  race_white: 11690
  race_black: 180
  race_asian: 0
  race_native: 0
  hispanic: 79
  bachelors_plus: 1784
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/senate/10"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wv/districts/house/40"
    rel: in-district
    area_weight: 0.9988
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Monroe County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12386 |
| Under 18 | 2628 |
| 18–64 | 6648 |
| 65+ | 3110 |
| Median household income | 56750 |
| Poverty rate | 13.97 |
| Homeownership rate | 86.86 |
| Unemployment rate | 4.77 |
| Median home value | 156300 |
| Gini index | 0.3976 |
| Vacancy rate | 25.98 |
| White | 11690 |
| Black | 180 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 79 |
| Bachelor's or higher | 1784 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 10](/us/states/wv/districts/senate/10.md) — 100% (state senate)
- [WV House District 40](/us/states/wv/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
