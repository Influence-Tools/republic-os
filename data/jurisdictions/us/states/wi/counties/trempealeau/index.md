---
type: Jurisdiction
title: "Trempealeau County, WI"
classification: county
fips: "55121"
state: "WI"
demographics:
  population: 30839
  population_under_18: 8221
  population_18_64: 16860
  population_65_plus: 5758
  median_household_income: 76313
  poverty_rate: 9.92
  homeownership_rate: 74.0
  unemployment_rate: 2.3
  median_home_value: 216700
  gini_index: 0.4008
  vacancy_rate: 6.69
  race_white: 26190
  race_black: 107
  race_asian: 142
  race_native: 346
  hispanic: 3997
  bachelors_plus: 5745
districts:
  - to: "us/states/wi/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/10"
    rel: in-district
    area_weight: 0.638
  - to: "us/states/wi/districts/senate/32"
    rel: in-district
    area_weight: 0.2165
  - to: "us/states/wi/districts/senate/31"
    rel: in-district
    area_weight: 0.1454
  - to: "us/states/wi/districts/house/29"
    rel: in-district
    area_weight: 0.638
  - to: "us/states/wi/districts/house/94"
    rel: in-district
    area_weight: 0.2165
  - to: "us/states/wi/districts/house/93"
    rel: in-district
    area_weight: 0.1454
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Trempealeau County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30839 |
| Under 18 | 8221 |
| 18–64 | 16860 |
| 65+ | 5758 |
| Median household income | 76313 |
| Poverty rate | 9.92 |
| Homeownership rate | 74.0 |
| Unemployment rate | 2.3 |
| Median home value | 216700 |
| Gini index | 0.4008 |
| Vacancy rate | 6.69 |
| White | 26190 |
| Black | 107 |
| Asian | 142 |
| Native | 346 |
| Hispanic/Latino | 3997 |
| Bachelor's or higher | 5745 |

## Districts

- [WI-03](/us/states/wi/districts/03.md) — 100% (congressional)
- [WI Senate District 10](/us/states/wi/districts/senate/10.md) — 64% (state senate)
- [WI Senate District 32](/us/states/wi/districts/senate/32.md) — 22% (state senate)
- [WI Senate District 31](/us/states/wi/districts/senate/31.md) — 15% (state senate)
- [WI House District 29](/us/states/wi/districts/house/29.md) — 64% (state house)
- [WI House District 94](/us/states/wi/districts/house/94.md) — 22% (state house)
- [WI House District 93](/us/states/wi/districts/house/93.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
