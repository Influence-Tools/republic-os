---
type: Jurisdiction
title: "Chaves County, NM"
classification: county
fips: "35005"
state: "NM"
demographics:
  population: 64217
  population_under_18: 15799
  population_18_64: 37849
  population_65_plus: 10569
  median_household_income: 52938
  poverty_rate: 24.29
  homeownership_rate: 71.29
  unemployment_rate: 5.03
  median_home_value: 156400
  gini_index: 0.4985
  vacancy_rate: 11.73
  race_white: 34497
  race_black: 1054
  race_asian: 1005
  race_native: 1233
  hispanic: 37529
  bachelors_plus: 10555
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.4537
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.3518
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.1945
  - to: "us/states/nm/districts/senate/27"
    rel: in-district
    area_weight: 0.5169
  - to: "us/states/nm/districts/senate/32"
    rel: in-district
    area_weight: 0.3267
  - to: "us/states/nm/districts/senate/42"
    rel: in-district
    area_weight: 0.0897
  - to: "us/states/nm/districts/senate/33"
    rel: in-district
    area_weight: 0.0667
  - to: "us/states/nm/districts/house/64"
    rel: in-district
    area_weight: 0.3283
  - to: "us/states/nm/districts/house/66"
    rel: in-district
    area_weight: 0.2528
  - to: "us/states/nm/districts/house/54"
    rel: in-district
    area_weight: 0.1944
  - to: "us/states/nm/districts/house/58"
    rel: in-district
    area_weight: 0.1843
  - to: "us/states/nm/districts/house/59"
    rel: in-district
    area_weight: 0.04
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Chaves County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64217 |
| Under 18 | 15799 |
| 18–64 | 37849 |
| 65+ | 10569 |
| Median household income | 52938 |
| Poverty rate | 24.29 |
| Homeownership rate | 71.29 |
| Unemployment rate | 5.03 |
| Median home value | 156400 |
| Gini index | 0.4985 |
| Vacancy rate | 11.73 |
| White | 34497 |
| Black | 1054 |
| Asian | 1005 |
| Native | 1233 |
| Hispanic/Latino | 37529 |
| Bachelor's or higher | 10555 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 45% (congressional)
- [NM-01](/us/states/nm/districts/01.md) — 35% (congressional)
- [NM-02](/us/states/nm/districts/02.md) — 19% (congressional)
- [NM Senate District 27](/us/states/nm/districts/senate/27.md) — 52% (state senate)
- [NM Senate District 32](/us/states/nm/districts/senate/32.md) — 33% (state senate)
- [NM Senate District 42](/us/states/nm/districts/senate/42.md) — 9% (state senate)
- [NM Senate District 33](/us/states/nm/districts/senate/33.md) — 7% (state senate)
- [NM House District 64](/us/states/nm/districts/house/64.md) — 33% (state house)
- [NM House District 66](/us/states/nm/districts/house/66.md) — 25% (state house)
- [NM House District 54](/us/states/nm/districts/house/54.md) — 19% (state house)
- [NM House District 58](/us/states/nm/districts/house/58.md) — 18% (state house)
- [NM House District 59](/us/states/nm/districts/house/59.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
