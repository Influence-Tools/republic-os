---
type: Jurisdiction
title: "Schenectady County, NY"
classification: county
fips: "36093"
state: "NY"
demographics:
  population: 160369
  population_under_18: 34413
  population_18_64: 97326
  population_65_plus: 28630
  median_household_income: 79623
  poverty_rate: 13.27
  homeownership_rate: 64.04
  unemployment_rate: 5.77
  median_home_value: 235700
  gini_index: 0.4492
  vacancy_rate: 6.09
  race_white: 110883
  race_black: 16461
  race_asian: 7947
  race_native: 625
  hispanic: 13270
  bachelors_plus: 58582
districts:
  - to: "us/states/ny/districts/20"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/ny/districts/senate/46"
    rel: in-district
    area_weight: 0.8756
  - to: "us/states/ny/districts/senate/44"
    rel: in-district
    area_weight: 0.1242
  - to: "us/states/ny/districts/house/111"
    rel: in-district
    area_weight: 0.6815
  - to: "us/states/ny/districts/house/112"
    rel: in-district
    area_weight: 0.2325
  - to: "us/states/ny/districts/house/110"
    rel: in-district
    area_weight: 0.0859
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Schenectady County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 160369 |
| Under 18 | 34413 |
| 18–64 | 97326 |
| 65+ | 28630 |
| Median household income | 79623 |
| Poverty rate | 13.27 |
| Homeownership rate | 64.04 |
| Unemployment rate | 5.77 |
| Median home value | 235700 |
| Gini index | 0.4492 |
| Vacancy rate | 6.09 |
| White | 110883 |
| Black | 16461 |
| Asian | 7947 |
| Native | 625 |
| Hispanic/Latino | 13270 |
| Bachelor's or higher | 58582 |

## Districts

- [NY-20](/us/states/ny/districts/20.md) — 100% (congressional)
- [NY Senate District 46](/us/states/ny/districts/senate/46.md) — 88% (state senate)
- [NY Senate District 44](/us/states/ny/districts/senate/44.md) — 12% (state senate)
- [NY House District 111](/us/states/ny/districts/house/111.md) — 68% (state house)
- [NY House District 112](/us/states/ny/districts/house/112.md) — 23% (state house)
- [NY House District 110](/us/states/ny/districts/house/110.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
