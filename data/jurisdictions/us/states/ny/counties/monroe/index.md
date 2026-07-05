---
type: Jurisdiction
title: "Monroe County, NY"
classification: county
fips: "36055"
state: "NY"
demographics:
  population: 753753
  population_under_18: 153175
  population_18_64: 459074
  population_65_plus: 141504
  median_household_income: 76382
  poverty_rate: 13.65
  homeownership_rate: 63.66
  unemployment_rate: 4.94
  median_home_value: 213700
  gini_index: 0.4658
  vacancy_rate: 6.19
  race_white: 524918
  race_black: 107052
  race_asian: 29319
  race_native: 1232
  hispanic: 74960
  bachelors_plus: 316529
districts:
  - to: "us/states/ny/districts/25"
    rel: in-district
    area_weight: 0.4861
  - to: "us/states/ny/districts/senate/62"
    rel: in-district
    area_weight: 0.1384
  - to: "us/states/ny/districts/senate/54"
    rel: in-district
    area_weight: 0.1285
  - to: "us/states/ny/districts/senate/55"
    rel: in-district
    area_weight: 0.1188
  - to: "us/states/ny/districts/senate/56"
    rel: in-district
    area_weight: 0.1008
  - to: "us/states/ny/districts/house/139"
    rel: in-district
    area_weight: 0.1031
  - to: "us/states/ny/districts/house/135"
    rel: in-district
    area_weight: 0.1
  - to: "us/states/ny/districts/house/134"
    rel: in-district
    area_weight: 0.0938
  - to: "us/states/ny/districts/house/138"
    rel: in-district
    area_weight: 0.0882
  - to: "us/states/ny/districts/house/136"
    rel: in-district
    area_weight: 0.0319
  - to: "us/states/ny/districts/house/130"
    rel: in-district
    area_weight: 0.0252
  - to: "us/states/ny/districts/house/133"
    rel: in-district
    area_weight: 0.0224
  - to: "us/states/ny/districts/house/137"
    rel: in-district
    area_weight: 0.0219
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Monroe County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 753753 |
| Under 18 | 153175 |
| 18–64 | 459074 |
| 65+ | 141504 |
| Median household income | 76382 |
| Poverty rate | 13.65 |
| Homeownership rate | 63.66 |
| Unemployment rate | 4.94 |
| Median home value | 213700 |
| Gini index | 0.4658 |
| Vacancy rate | 6.19 |
| White | 524918 |
| Black | 107052 |
| Asian | 29319 |
| Native | 1232 |
| Hispanic/Latino | 74960 |
| Bachelor's or higher | 316529 |

## Districts

- [NY-25](/us/states/ny/districts/25.md) — 49% (congressional)
- [NY Senate District 62](/us/states/ny/districts/senate/62.md) — 14% (state senate)
- [NY Senate District 54](/us/states/ny/districts/senate/54.md) — 13% (state senate)
- [NY Senate District 55](/us/states/ny/districts/senate/55.md) — 12% (state senate)
- [NY Senate District 56](/us/states/ny/districts/senate/56.md) — 10% (state senate)
- [NY House District 139](/us/states/ny/districts/house/139.md) — 10% (state house)
- [NY House District 135](/us/states/ny/districts/house/135.md) — 10% (state house)
- [NY House District 134](/us/states/ny/districts/house/134.md) — 9% (state house)
- [NY House District 138](/us/states/ny/districts/house/138.md) — 9% (state house)
- [NY House District 136](/us/states/ny/districts/house/136.md) — 3% (state house)
- [NY House District 130](/us/states/ny/districts/house/130.md) — 3% (state house)
- [NY House District 133](/us/states/ny/districts/house/133.md) — 2% (state house)
- [NY House District 137](/us/states/ny/districts/house/137.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
