---
type: Jurisdiction
title: "McKinley County, NM"
classification: county
fips: "35031"
state: "NM"
demographics:
  population: 70431
  population_under_18: 19076
  population_18_64: 41643
  population_65_plus: 9712
  median_household_income: 47668
  poverty_rate: 33.24
  homeownership_rate: 69.78
  unemployment_rate: 9.04
  median_home_value: 78700
  gini_index: 0.4955
  vacancy_rate: 15.61
  race_white: 6884
  race_black: 326
  race_asian: 982
  race_native: 54775
  hispanic: 8585
  bachelors_plus: 8360
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9209
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.079
  - to: "us/states/nm/districts/senate/22"
    rel: in-district
    area_weight: 0.4918
  - to: "us/states/nm/districts/senate/4"
    rel: in-district
    area_weight: 0.2898
  - to: "us/states/nm/districts/senate/3"
    rel: in-district
    area_weight: 0.1572
  - to: "us/states/nm/districts/senate/30"
    rel: in-district
    area_weight: 0.0612
  - to: "us/states/nm/districts/house/69"
    rel: in-district
    area_weight: 0.3573
  - to: "us/states/nm/districts/house/6"
    rel: in-district
    area_weight: 0.2659
  - to: "us/states/nm/districts/house/5"
    rel: in-district
    area_weight: 0.2359
  - to: "us/states/nm/districts/house/9"
    rel: in-district
    area_weight: 0.1407
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# McKinley County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70431 |
| Under 18 | 19076 |
| 18–64 | 41643 |
| 65+ | 9712 |
| Median household income | 47668 |
| Poverty rate | 33.24 |
| Homeownership rate | 69.78 |
| Unemployment rate | 9.04 |
| Median home value | 78700 |
| Gini index | 0.4955 |
| Vacancy rate | 15.61 |
| White | 6884 |
| Black | 326 |
| Asian | 982 |
| Native | 54775 |
| Hispanic/Latino | 8585 |
| Bachelor's or higher | 8360 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 92% (congressional)
- [NM-02](/us/states/nm/districts/02.md) — 8% (congressional)
- [NM Senate District 22](/us/states/nm/districts/senate/22.md) — 49% (state senate)
- [NM Senate District 4](/us/states/nm/districts/senate/4.md) — 29% (state senate)
- [NM Senate District 3](/us/states/nm/districts/senate/3.md) — 16% (state senate)
- [NM Senate District 30](/us/states/nm/districts/senate/30.md) — 6% (state senate)
- [NM House District 69](/us/states/nm/districts/house/69.md) — 36% (state house)
- [NM House District 6](/us/states/nm/districts/house/6.md) — 27% (state house)
- [NM House District 5](/us/states/nm/districts/house/5.md) — 24% (state house)
- [NM House District 9](/us/states/nm/districts/house/9.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
